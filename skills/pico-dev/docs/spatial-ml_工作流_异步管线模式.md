SpatialML 的调用本质上都是异步的：实例创建、会话初始化、场景加载，以及每一次提交都需要花费时间，应该放在主线程之外执行。本页展示 [SuperResolutionApp](samples-super-resolution) 使用的协程模式，核心是它的 `AsyncPipelineRunner` 辅助类。
## 为什么用协程

* `SpatialMLInstance.create(...)` 会在运行时尚未 `ready` 之前就返回；你需要用 `delay` 来轮询。
* 场景加载（`newSceneFromGLTFSuspend`）和回读都提供了面向协程的 `suspend` 版本。
* 逐帧循环就是一个在每次提交之间带 `delay` 的 `while` 循环。

把所有这些工作都放在一个你自己掌控的 `CoroutineScope` 中运行——示例使用 `viewModelScope`，这样工作会随着 ViewModel 一起被取消。
## 将关闭视为取消
管线创建可能仍在等待原生模型初始化，而此时用户已经关闭了窗口或离开了功能。当前 SDK 在 `runModelInference` 构建期间将后端断开报告为：
```text
SecureMR backend connection was lost while creating model inference
```

当该异常是因为你的生命周期作用域正在关闭而发生时，请将已知的关闭场景转换为 `CancellationException`，而不是将其作为功能故障暴露出来：
```kotlin
private const val BACKEND_CONNECTION_LOST =
    "SecureMR backend connection was lost while creating model inference"

try {
    runModelInference(
        modelName = "style_predictor",
        modelType = Pipeline.ModelInferenceType.LITE_RT_NPU,
        modelBinary = modelMemory,
        inputs = inputs,
        outputs = outputs,
    )
} catch (error: SpatialMLException) {
    if (error.message == BACKEND_CONNECTION_LOST && !scope.isActive) {
        throw CancellationException("pipeline creation stopped during shutdown", error)
    }
    throw error
}
```

仅在关闭确实正在进行时才进行转换。如果在功能活跃期间出现相同的消息，则表明发生了意外的后端断开，应当保持为错误。
## 延迟创建会话，随处等待它
把会话创建成一个 `Deferred`，只创建一次，然后在任何需要它的地方 `await()`。这样可以让多条独立的管线共享同一个会话，而不会在初始化上产生竞争：
```kotlin
private val sessionDeferred = scope.async {
    SpatialMLInstance.create(appContext)
        .also { while (!it.ready) delay(100) }
        .createSession(InitInfo(/* ... */))!!
}
```

## AsyncPipelineRunner
示例把管线的创建和提交都封装进了一个小型辅助类。你把作用域、延迟创建的会话，以及一个用于构建图的 lambda 传给它；它会惰性地创建管线，并对外暴露两个运行方法。
```kotlin
class AsyncPipelineRunner(
    val scope: CoroutineScope,
    session: Deferred<SpatialMLSession>,
    pipelineCreator: (Pipeline, MutableMap<PipelineTensorPlaceholder, GlobalTensor>) -> Unit,
)
```


* 图只在会话就绪之后、在 `scope.async { ... }` 内部构建一次。
* 一个 `placeholderMap` 会与管线一起保存，并在每次 `submit` 时传入（参见[执行模型](concepts-execution-model#%E5%8D%A0%E4%BD%8D%E7%AC%A6%E4%B8%8E%E7%BB%91%E5%AE%9A)）。

### 持续运行（逐帧循环）
`runContinuously(frequency, startAfter, tensorMapUpdate)` 会按固定频率提交图，直到被取消为止，并内置了失败容忍机制：
```kotlin
fun runContinuously(frequency: Int, startAfter: Deferred<Pipeline.RunTask>? = null, /* ... */) =
    scope.launch {
        val intervalMs = (1000 / frequency).toLong()
        val pipeline = pipelineDeferred.await()
        var task: Pipeline.RunTask? = startAfter?.await()   // wait for prior stage
        var failureAllowance = 5
        while (failureAllowance > 0) {
            try {
                pipeline.submit(placeholderMap, null, task)
                failureAllowance = 5                        // reset on success
            } catch (e: SpatialMLException) {
                failureAllowance -= 1                       // give up after 5 in a row
            }
            task = null
            delay(intervalMs)
        }
    }
```

用法——以 10 Hz 启动主循环，但要等仿射设置阶段完成之后再开始：
```text
superResolution.mainPipeline.runContinuously(frequency = 10, startAfter = affineTask)
```

### 重置数值后运行一次
`runOnceAfterValueReset(prevTask, tensorMapUpdate, valueReSetter)` 会在更新张量数值之后把图提交一次——用于像示例中缩放变化这样的偶发性重新计算：
```kotlin
fun setUpscaleFactor(ratio: Float, prevTask: Deferred<Pipeline.RunTask>? = null) =
    affinePipeline.runOnceAfterValueReset(prevTask) {
        // write new source points into zoomPoints.tensorResource ...
        zoomPoints.tensorResource = mem
    }   // returns Deferred<RunTask> you can chain into the next stage
```

## 用 RunTask 为各阶段排序
每个运行方法都会返回（或接受）一个 `Deferred<Pipeline.RunTask>`。把一个阶段的 task 传给下一个阶段的 `startAfter` / `prevTask`，就构建出了运行时通过 [waitFor](concepts-execution-model#%E7%AE%A1%E7%BA%BF%E6%8E%92%E5%BA%8F) 强制执行的依赖链：
```kotlin
val affineTask = superResolution.setUpscaleFactor(initRatio, superResolution.initTask)
superResolution.mainPipeline.runContinuously(10, affineTask)
```


## 准则

* 把所有 SpatialML 相关工作都放在一个与你的 UI 生命周期绑定的、可取消的作用域中。
* 在释放功能之前取消该作用域；仅在作用域正在关闭时才将已知的模型创建后端丢失场景视为取消。
* 每个图只构建一次，反复提交。不要每帧都重新构建管线。
* 容忍提交时偶发的 `SpatialMLException`（示例允许连续失败 5 次才停止）。
* 通过 `tensorMapUpdate` 更新 `placeholderMap`，以便在不同的全局张量之间复用同一个图。

## 延伸阅读

* [执行模型](concepts-execution-model)——提交、条件与执行顺序。
* [SuperResolutionApp](samples-super-resolution)——这些模式在完整应用中的运用。
* [submit](reference-operators-submit)[ 算子卡片](reference-operators-submit)

