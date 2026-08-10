管线只是对一项工作的描述；在你提交它之前不会运行任何东西。本页说明提交是如何工作的、图如何通过占位符消费共享数据，以及如何对多个管线排序以确保它们按正确的顺序运行。
## 提交管线
你通过调用 [submit(...)](reference-operators-submit) 来运行一个图，该调用会将一次执行加入队列并返回一个 [Pipeline.RunTask](reference-core-api#pipeline-runtask)：
```kotlin
val task: Pipeline.RunTask = pipeline.submit(
    parameters = placeholderMap,   // placeholder -> GlobalTensor bindings for this run
    condition = null,              // optional GlobalTensor gate
    waitFor = previousTask,        // optional dependency to run after
)
```

这三个参数构成了完整的执行契约：

* `parameters` —— 将图中的每个[占位符](#%E5%8D%A0%E4%BD%8D%E7%AC%A6%E4%B8%8E%E7%BB%91%E5%AE%9A)绑定到本次运行所使用的具体 `GlobalTensor`。
* `condition` —— 一个可选的 `GlobalTensor`，用于控制本次运行是否执行。
* `waitFor` —— 一个可选的 `RunTask`，本次提交必须在其之后运行，用于[对管线排序](#%E7%AE%A1%E7%BA%BF%E6%8E%92%E5%BA%8F)。

由于搭建（setup）与提交是分离的，每次运行的开销只是一次提交；通常你会重复提交同一个图（参见[异步管线模式](workflows-async-pipeline-patterns)）。
## 占位符与绑定
用 [newLocalTensor](reference-operators-new-local-tensor) 创建的本地张量用来保存中间值。若要将**共享**数据（即[全局张量](concepts-tensors-and-shapes#%E5%85%A8%E5%B1%80%E5%BC%A0%E9%87%8F%E4%B8%8E%E6%9C%AC%E5%9C%B0%E5%BC%A0%E9%87%8F)）输入到图中，图会声明一个 [PipelineTensorPlaceholder](reference-operators-new-placeholder)，然后你在提交时通过 `parameters` map 将一个真实的 `GlobalTensor` 绑定给它：
```kotlin
// map maintained alongside the pipeline
val placeholderMap = mutableMapOf<PipelineTensorPlaceholder, GlobalTensor>()

// ... graph creates placeholders and adds them to the map ...

// each submit can bind different global tensors to the same placeholders
pipeline.submit(placeholderMap, null, task)
```

这种间接绑定让同一个管线可以在不同运行之间操作不同的全局张量——在提交前更新 map，同一个图就能处理新的数据。示例代码中的 [AsyncPipelineRunner](workflows-async-pipeline-patterns) 正是为此暴露了一个 `tensorMapUpdate` 回调。
**写入全局张量不一定需要占位符**
管线可以直接写入它闭包捕获的 `GlobalTensor`（正如示例中对 `dynamicTexture` 和 `zoomAffine` 的处理方式）。占位符适用于更通用的场景，即你希望在提交时重新绑定某个阶段使用的是哪个全局张量。
## 管线排序
实际应用通常不止一个管线：一个初始化管线、一个逐帧管线，以及偶尔出现的一次性管线。`waitFor` 通过让一次提交依赖另一次提交的 `RunTask` 来把它们串联起来。

示例代码正是这样搭建这条链的：
```kotlin
// 1. init pipeline runs first (Secure Mode only)
val initTask = /* submit init pipeline */

// 2. affine pipeline runs after init
val affineTask = superResolution.setUpscaleFactor(initRatio, initTask)

// 3. main pipeline runs continuously after the affine matrix is ready
superResolution.mainPipeline.runContinuously(frequency = 10, startAfter = affineTask)
```

每个阶段都把自己的 `Deferred<RunTask>` 作为 `waitFor` / `startAfter` 传给下一个阶段，因此运行时在一次性的初始化完成之前不会启动主循环。
## 条件
`condition` 参数根据一个 `GlobalTensor` 值来控制执行，让图可以在运行时决定是否运行其效果。它适用于那些原本需要在应用代码中重新构建或重新提交图才能实现的分支逻辑。当不需要门控时，传入 `null` 即可（正如示例所做的那样）。
## 整合到一起

## 延伸阅读

* [异步管线模式](workflows-async-pipeline-patterns) —— 从协程中运行提交操作。
* [submit](reference-operators-submit)[ 算子卡片](reference-operators-submit) —— 完整的签名与约束条件。
* [张量与形状](concepts-tensors-and-shapes) —— 全局张量与本地张量，以及占位符。

