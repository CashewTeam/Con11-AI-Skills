你在 Kotlin 中打交道的核心 SpatialML 类型，按使用顺序排列。类型位于 `com.pico.spatial.ml.securemr`；回读相关类型位于 `com.pico.spatial.ml.readback`。`Pipeline` 上的算子方法请参见[算子目录](reference-operator-catalog)；张量的 init-info 和枚举请参见[张量类型与枚举](reference-tensor-types-and-enums)。
## SpatialMLInstance
面向整个进程的运行时入口。
```kotlin
val instance = SpatialMLInstance.create(context)   // asynchronous
while (!instance.ready) delay(100)                 // poll until usable
val session = instance.createSession(initInfo)     // open a session
```

| 成员 | 说明 |
| --- | --- |
| `SpatialMLInstance.create(context)` | 创建实例。会在运行时就绪之前就返回。 |
| `ready: Boolean` | 运行时可用时为 `true`。在调用 `createSession` 之前轮询它。 |
| `createSession(initInfo): SpatialMLSession?` | 使用给定配置打开一个会话。 |
只创建一次实例并复用它。请在主线程之外执行这一步——参见[异步管线模式](workflows-async-pipeline-patterns)。
## SpatialMLSession
一个已配置的运行时上下文，拥有张量、场景和管线。
```kotlin
val session = instance.createSession(
    SpatialMLSession.InitInfo(
        imageWidth = 512, imageHeight = 512,
        containerWidth = 1200, containerHeight = 1200, containerDepth = 200,
    )
)!!

val pipeline = session.newPipeline()
val global   = session.newGlobalTensor(initInfo)
val scene    = session.newSceneFromGLTFSuspend("Display512.glb")
```

| 成员 | 说明 |
| --- | --- |
| `newPipeline(): Pipeline` | 创建一个空管线，供你在其中搭建图。 |
| `newGlobalTensor(initInfo): GlobalTensor` | 创建一个会话范围的张量（可共享、可回读）。 |
| `newSceneFromGLTF(assetOrMem): GlobalTensor` | 将一个 glTF 场景加载为全局张量。 |
| `newSceneFromGLTFSuspend(...)` | 供协程使用的 `suspend` 版本。 |
| `loadPipelinePackageFromAssets(assetRoot, externalGlobals): PipelinePackageBundle` | 从应用 assets 中加载一个现成的 [管线包](reference-pipeline-packages)（即 "Pipeline Zoo" 包）。 |
### SpatialMLSession.InitInfo
```text
SpatialMLSession.InitInfo(
    imageWidth: Int,
    imageHeight: Int,
    containerWidth: Int,
    containerHeight: Int,
    containerDepth: Int,
    containerType: ContainerType = ContainerType.VOLUMETRIC,
)
```

| 字段 | 含义 |
| --- | --- |
| `imageWidth`、`imageHeight` | 运行时提供给 [rectifiedVSTAccess](reference-operators-rectified-vst-access) 的 VST 图像尺寸。 |
| `containerWidth`、`containerHeight`、`containerDepth` | 运行时所拥有场景容器的尺寸。在[安全模式](concepts-secure-and-readback-modes)下为非零值；在回读模式下为 `0`（或使用 `DISABLED` 容器）。 |
| `containerType` | 容器形状——参见 [ContainerType](#containertype)。默认值为 `VOLUMETRIC`。 |
#### ContainerType
| 值 | 含义 |
| --- | --- |
| `VOLUMETRIC` | 一个立体（3-D）盒状容器（默认值）。盒外的内容会被裁剪，除非添加了[portal](#addportal)。使用 `containerDepth`。 |
| `PLANAR` | 一个平面（2-D）容器。`containerDepth` 会被忽略；Z 轴范围受限。 |
| `DISABLED` | 没有运行时容器——只有应用自己的容器。用于回读模式。 |
参见[容器与传送门](concepts-containers-and-portals)了解容器选择指南。
#### addPortal()
`InitInfo.addPortal(): InitInfo` 在**立体（volumetric）**容器的背面添加一个隐藏的 portal 面板，这样锚定在容器边界之外的 3D 内容可以透过该面板保持可见。它是 [CameraAnchor](reference-tensor-types-and-enums#scenegraphproperty) 追踪的标准搭档——例如，让锚定在某个被检测物体上的画面在该物体移出盒子范围时仍保持可见。
这不会创建一个单独的容器类型：容器仍然是 `VOLUMETRIC`。与常规 Volume 相比，它保留了相同的有界盒子，但在该盒子之外添加了背面 portal 作为查看超出范围内容的窗口。对有意限制在边界内的内容使用常规 Volume；对位置可能超出配置体积的被追踪、相机锚定的内容使用 Portal。
它要求容器类型为 `VOLUMETRIC` 且宽/高/深均为正值，否则会抛出异常。它返回同一个 `InitInfo`，因此可以在构造调用中链式使用：
```kotlin
val session = instance.createSession(
    SpatialMLSession.InitInfo(
        imageWidth = 580, imageHeight = 326,
        containerWidth = 1000, containerHeight = 1000, containerDepth = 10,
        containerType = SpatialMLSession.ContainerType.VOLUMETRIC,
    ).addPortal()
)!!
```

关于行为、限制和选择指南，请参见[容器与传送门](concepts-containers-and-portals)。
## Pipeline
由算子调用组成的有序图。只搭建一次，可[提交](reference-operators-submit)多次。
```kotlin
session.newPipeline().apply {
    val t = newLocalTensor(initInfo)     // create local tensors
    rectifiedVSTAccess(rightImageResult = t)   // add operator stages
    // ...
    submit(placeholderMap, condition, waitFor)  // execute
}
```

`Pipeline` 成员的分类（均记录在[算子目录](reference-operator-catalog)中）：

* **张量创建** —— `newLocalTensor`、`newPlaceholder`、`newPlaceholderLike`、`newSceneFromGLTF`。
* **算子** —— 相机/传感器访问、图像变换、数学运算、比较、几何、场景输出、音频、脚本。
* **执行** —— `submit(...)`。

`newLocalTensor` 为常量数据提供了便捷重载，因此你不必手动分配 init-info 和 `SharedMemory`。除了 `newLocalTensor(config: Tensor.InitInfo)` 之外，还有一些重载可以接收字面值或数组，并构建出对应的常量张量：
```text
newLocalTensor(0xF.toByte())                       // scalar byte (e.g. a visibility flag)
newLocalTensor(floatArrayOf(0.02f, 0.02f, 0.001f)) // float vector (e.g. a scale)
newLocalTensor("hello")                            // string tensor for text output
```

已提供 `Byte`、`Int`/`IntArray`、`Short`/`ShortArray`、`Float`/`FloatArray`、`Double`/`DoubleArray`、`String`、`Point`/`Array<Point>`，以及 `Color`/`Array<Color>` 的重载。
### Pipeline.RunTask
`submit(...)` 返回的句柄。把它作为另一次提交的 `waitFor` 传入，即可[对管线排序](concepts-execution-model#%E7%AE%A1%E7%BA%BF%E6%8E%92%E5%BA%8F)。在协程代码中，你通常会持有一个 `Deferred<Pipeline.RunTask>`。
### Pipeline.ModelNodeEncoding
将一个模型节点名绑定到一个张量，用于[推理](reference-operators-run-model-inference)。
```kotlin
Pipeline.ModelNodeEncoding(val nodeName: String, val tensor: Tensor)
```

### Pipeline.ModelInferenceType
选择推理加速器——`LITE_RT_CPU`、`LITE_RT_GPU`、`LITE_RT_NPU`。模型二进制文件始终是 TensorFlow Lite FlatBuffer（`.tflite`）。参见[张量类型与枚举](reference-tensor-types-and-enums#pipeline-modelinferencetype)。
## Tensor 与 GlobalTensor
`Tensor` 是图数据的基础类型；`GlobalTensor` 是 session 范围的张量。
| 成员 | 说明 |
| --- | --- |
| `config` | 创建该张量时所用的 init-info（可复用它来创建匹配的张量）。 |
| `tensorResource: SharedMemory?` | 底层内存。设置它可以把常量数据加载到张量中。 |

* **本地张量**来自 `pipeline.newLocalTensor(...)` / `newPlaceholder(...)`。
* **全局张量**来自 `session.newGlobalTensor(...)` / `newSceneFromGLTF(...)`，也是唯一可以[回读](workflows-read-back-results)的张量。

完整的模型请参见[张量与形状](concepts-tensors-and-shapes)，所有 init-info 请参见[张量类型与枚举](reference-tensor-types-and-enums)。
## PipelineTensor 与 PipelineTensorPlaceholder

* `PipelineTensor` —— 存在于管线内部的张量（`newLocalTensor` 的返回类型）。
* `PipelineTensorPlaceholder` —— `GlobalTensor` 的占位符，在[提交时](concepts-execution-model#%E5%8D%A0%E4%BD%8D%E7%AC%A6%E4%B8%8E%E7%BB%91%E5%AE%9A)通过 `parameters` map 绑定。

## SharedMemory
标准的 Android `android.os.SharedMemory`，用于在你的应用和运行时之间传递字节数据——模型字节、点数据以及回读缓冲区。典型的写入方式：
```kotlin
SharedMemory.create("name", byteSize).use { mem ->
    val buf = mem.mapReadWrite().order(ByteOrder.nativeOrder())
    /* put data */
    SharedMemory.unmap(buf)
    tensor.tensorResource = mem
}
```

## 回读
`com.pico.spatial.ml.readback` 中定义在 `GlobalTensor` 上的扩展函数：
| 函数 | 返回类型 |
| --- | --- |
| `readbackContent()` / `readbackContentSuspend()` | `TensorContent` |
| `readbackAsTextureResource()` / `readbackAsTextureResourceSuspend()` | `TextureResource` |
### TensorContent
包装回读字节数据的 `AutoCloseable`。
| 成员 | 说明 |
| --- | --- |
| `buffer` | 持有数据的 `ByteBuffer`（由 `SharedMemory` 支撑）。 |
| `close()` | 释放本地（native）内存。请始终使用 `use { ... }`。 |
参见[将数据回读到应用](workflows-read-back-results)。
## SpatialMLException
在运行时/提交失败时抛出。持续循环通常会容忍几次连续失败后再停止——参见[异步管线模式](workflows-async-pipeline-patterns)。
## 管线包类型
当你加载一个预先构建好的 [管线包](reference-pipeline-packages)时，由 [loadPipelinePackageFromAssets](#spatialmlsession) 返回。这些类型你不需要自己构造——只需要读取它们。
### PipelinePackageBundle
| 成员 | 说明 |
| --- | --- |
| `manifest: PipelinePackageManifest` | 解析后的 manifest。 |
| `pipelines: Map<String, PipelinePackagePipeline>` | 已构建好的管线，以 manifest 中的管线 `id` 为键。 |
| `globalTensors: Map<String, GlobalTensor>` | 该包实例化出的全局张量（在其各个管线之间共享），以张量名称为键。 |
| `detectionTensor: String?` | 如果 manifest 中声明了检测输出张量，这里是它的名称。 |
### PipelinePackagePipeline
| 成员 | 说明 |
| --- | --- |
| `id: String` | 来自 manifest 的管线 id。 |
| `pipeline: Pipeline` | 已构建好的管线——[提交](reference-operators-submit)它。 |
| `submitBindings: Map<PipelineTensorPlaceholder, GlobalTensor>` | 传给 `pipeline.submit(...)` 的占位符→全局张量绑定。 |
| `inputs: List<String>` / `outputs: List<String>` | 该管线声明为输入/输出的张量名称。 |
### PipelinePackageManifest
| 成员 | 说明 |
| --- | --- |
| `formatVersion: Int` | 包格式版本（当前为 `1`）。 |
| `detectionTensor: String?` | 可选的检测输出张量名称。 |
加载与提交流程请参见[使用管线包](workflows-use-pipeline-packages)，磁盘存储格式请参见[管线包格式](reference-pipeline-packages)。
## 延伸阅读

* [算子目录](reference-operator-catalog) —— 所有 `Pipeline` 方法。
* [张量类型与枚举](reference-tensor-types-and-enums) —— init-info 与枚举。
* [运行时模型](concepts-mental-model) —— 这些类型之间的关系。

