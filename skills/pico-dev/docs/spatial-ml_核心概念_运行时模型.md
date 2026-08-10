SpatialML 把机器学习和计算机视觉任务作为一个**图**来运行，由运行时代表你执行。本页说明你要打交道的对象及其相互配合方式，以便文档其余部分可以专注于具体任务。
## 五个基本构件
| 概念 | Kotlin 类型 | 它是什么 |
| --- | --- | --- |
| Instance | [SpatialMLInstance](reference-core-api#spatialmlinstance) | 面向整个进程的运行时入口。只创建一次，在 `ready` 为 `true` 时即可使用。 |
| Session | [SpatialMLSession](reference-core-api#spatialmlsession) | 一个已配置的运行时上下文（图像尺寸和容器尺寸）。拥有张量、场景和管线。 |
| Pipeline | [Pipeline](reference-core-api#pipeline) | 由张量上的算子调用组成的有序图。只搭建一次，可多次提交。 |
| Tensor | [Tensor](concepts-tensors-and-shapes) / [GlobalTensor](concepts-tensors-and-shapes#%E5%85%A8%E5%B1%80%E5%BC%A0%E9%87%8F%E4%B8%8E%E6%9C%AC%E5%9C%B0%E5%BC%A0%E9%87%8F) | 在算子之间流动的带类型多维数据。 |
| Operator | [Pipeline](reference-operator-catalog)[ 方法](reference-operator-catalog) | 单个图阶段，例如 `rectifiedVSTAccess(...)` 或 `runModelInference(...)`。 |

## 算子是 Pipeline 上的方法
最需要牢记的一点是：**在 Kotlin SDK 中，"算子"就是你在 `Pipeline` 上调用的方法。**你不需要实例化算子对象，而是调用一些方法，这些方法会给图添加一个阶段，并返回结果张量（或写入你传进去的张量）。
```kotlin
session.newPipeline().run {
    // each call below adds one operator stage to this pipeline's graph
    val rightEye = newLocalTensor(
        MultiDimensionalInitInfo(DataType.UINT8, intArrayOf(512, 512), channel = 3)
    )
    rectifiedVSTAccess(rightImageResult = rightEye)   // camera access operator

    val small = newLocalTensor(
        MultiDimensionalInitInfo(DataType.UINT8, intArrayOf(128, 128), channel = 3)
    )
    applyAffine(zoomAffine, rightEye, small)          // image transform operator

    submit(mapOf(), null, null)                        // execute the graph
}
```

[算子目录](reference-operator-catalog)以卡片式的事实条目记录了这里每一个方法。
## 只需搭建一次，多次提交
管线是一份**工作描述**，而不是一次性调用。你只搭建一次图（通常在初始化阶段），然后反复提交它——例如以固定频率每帧提交一次——而无需重新搭建。

* 搭建图：在 `Pipeline` 上调用算子方法。
* 运行图：调用 [submit(...)](reference-operator-catalog) 将一次执行加入队列，返回一个 [RunTask](reference-core-api#pipeline-runtask)。
* 重复：再次提交。示例代码通过 [AsyncPipelineRunner.runContinuously](workflows-async-pipeline-patterns) 以 10 Hz 的频率提交其主管线。

正是这种分离让这套 API 高效：图的搭建成本只需支付一次，每帧的成本只是一次提交。
## 数据如何进出图

* **输入**：相机数据通过 [rectifiedVSTAccess](reference-operators-rectified-vst-access) 和 [getDepthMap](reference-operators-get-depth-map) 等算子进入。常量数据通过在提交前写入张量的 `tensorResource`（[SharedMemory](reference-core-api#sharedmemory)）进入。模型字节通过 [runModelInference](reference-operators-run-model-inference) 进入。
* **输出**：结果通过[场景图算子](workflows-drive-scene-graph-output)驱动 SpatialEngine 从而到达用户，或者通过[回读](workflows-read-back-results)返回到你的应用代码中（取决于你选择的[模式](concepts-secure-and-readback-modes)）。

## 全局张量与本地张量

* **本地张量**（[newLocalTensor](reference-operators-new-local-tensor)、[newPlaceholder](reference-operators-new-placeholder)）属于单个管线，在一次运行期间保存中间值。
* **全局张量**（[session.newGlobalTensor](reference-core-api#spatialmlsession)、来自 `newSceneFromGLTF` 的场景）位于 session 上，在多次运行之间持续存在。它们是独立管线之间共享数据的方式，也是你**唯一**可以[回读](workflows-read-back-results)的张量。

完整的张量模型请参见[张量与形状](concepts-tensors-and-shapes)；关于占位符如何在提交时把全局张量绑定进管线，请参见[执行模型](concepts-execution-model)。
## 延伸阅读

* [空间模式](concepts-spatial-mode) —— SpatialML 应用是如何组织和渲染的。
* [安全模式与回读模式](concepts-secure-and-readback-modes) —— 你可以选择的隐私边界。
* [张量与形状](concepts-tensors-and-shapes) —— 张量数据模型。
* [执行模型](concepts-execution-model) —— 提交、条件与依赖关系。

