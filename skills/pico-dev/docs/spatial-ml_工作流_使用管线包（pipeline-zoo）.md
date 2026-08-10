**管线包**是一个现成的 SpatialML 图——包含模型、管线、张量以及任何 glTF 场景——被打包成应用资源，一次调用即可加载。这是让相机驱动的 ML 功能跑起来最快的方式：无需自己编写每一个算子，只需把一个包放进 `assets/`、加载它，再提交它的各条管线即可。这些包可以来自 **Pipeline Zoo**（预置好的包，例如人脸检测），也可以是你自己编写的。
**如果已有包能满足需求，从这里开始**
如果某个 Pipeline Zoo 包已经覆盖了你的使用场景，你可以在不写任何算子代码的情况下就把功能上线。只有当你需要自己构建或扩展图时，才需要用到[算子目录](reference-operator-catalog)和[工作流](workflows-prepare-image-data)。
## 仅需一次调用
```kotlin
import com.pico.spatial.ml.securemr.loadPipelinePackageFromAssets

val bundle = session.loadPipelinePackageFromAssets("SpatialML/face-mediapipe-pipeline")
```

`loadPipelinePackageFromAssets` 是 [SpatialMLSession](reference-core-api#spatialmlsession) 上的一个扩展函数：
```kotlin
fun SpatialMLSession.loadPipelinePackageFromAssets(
    assetRoot: String,
    externalGlobals: Map<String, GlobalTensor> = emptyMap(),
): PipelinePackageBundle
```


* `assetRoot`——包含该包 `manifest.json` 的资源目录（开头/结尾的斜杠会被去除）。
* `externalGlobals`——可选的、由应用自己创建的[全局张量](concepts-tensors-and-shapes#%E5%85%A8%E5%B1%80%E5%BC%A0%E9%87%8F%E4%B8%8E%E6%9C%AC%E5%9C%B0%E5%BC%A0%E9%87%8F)，以张量名称为键，绑定进该包中，而不是让它自行创建（每一个都必须与包内张量的配置完全一致）。
* 需要 Android API 27+（`O_MR1`）。会抛出 `IOException`（资源相关问题）或 [SpatialMLException](reference-core-api#spatialmlexception)（schema、模式或张量不匹配问题）。

返回结果是一个 [PipelinePackageBundle](reference-core-api#pipelinepackagebundle)：解析出的 `manifest`、一个以 id 为键的 `pipelines` 映射，以及一个 `globalTensors` 映射，包含该包实体化并在各条管线之间共享的张量。
## 仅限空间模式
只有当 manifest 的 `runtime.supported_modes` 中包含 `"spatial"` 时，加载器才会接受该包。仅支持 XR 的包会被以 `supported_modes must include spatial` 拒绝。参见 [管线包格式](reference-pipeline-packages#%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B8%8E%E6%A8%A1%E5%BC%8F)。
## 先加载，再提交——四个步骤
一个包会给你已经构建好的管线和共享张量，但执行过程由**你**来掌控：查找所需的各个部分、接好任何应用侧的场景，然后每帧按依赖顺序提交包内的管线。[FaceDetection 示例](samples-face-detection)做的正是这件事。
### 1. 查找管线与共享张量
```kotlin
val detection = bundle.pipelines["detection"]
    ?: error("package has no 'detection' pipeline")
val display = bundle.pipelines["display"]
    ?: error("package has no 'display' pipeline")

// tensors the package materialized that you want to drive yourself
val framePose  = bundle.globalTensors["frame_pose"]   // a 4x4 transform output
    ?: error("frame_pose was not materialized")
val frameScene = bundle.globalTensors["frame_gltf"]   // a glTF scene loaded from the package
    ?: error("frame_gltf was not materialized")
```

每个 [PipelinePackagePipeline](reference-core-api#pipelinepackagepipeline) 都会暴露它构建好的 `pipeline`、要传给 `submit` 的 `submitBindings`（占位符→全局张量的映射），以及它声明的 `inputs`/`outputs`。
### 2. 一次性设置应用侧场景
会产生位姿的包通常会附带一个 glTF，运行时会把它实体化到 `globalTensors` 中。请在循环开始之前、在你自己的初始化管线中完成一次性的场景设置——锚定模式、初始缩放、可见性：
```kotlin
val initTask = session.newPipeline().run {
    updateSceneGraphProperty(frameScene, "/", SceneGraphProperty.CameraAnchor.Follow,
        newLocalTensor(identityMatrix4x4))
    updateSceneGraphProperty(frameScene, "/", SceneGraphProperty.Transform.Scale,
        newLocalTensor(floatArrayOf(0.02f, 0.02f, 0.001f)))
    switchSceneVisibility(frameScene, newLocalTensor(0xF.toByte()))
    submit(emptyMap(), null, null)
}
```

由于该包的位姿会落在一个共享的全局张量中，一个很小的应用管线就可以把该张量绑定到场景的 [CameraAnchor.Follow](reference-tensor-types-and-enums#scenegraphproperty) 属性上，让实体自动跟踪检测结果：
```kotlin
val framePipeline = session.newPipeline().apply {
    updateSceneGraphProperty(frameScene, "/", SceneGraphProperty.CameraAnchor.Follow, framePose)
}
```

**锚定要搭配 portal 使用**
常规 Volume 会在其边界处裁剪被锚定的内容。当被追踪的内容可能移出该体积范围时，请在创建会话时加上 [addPortal()](concepts-containers-and-portals)，让它可以通过背面 portal 保持可见。容器仍然是 `VOLUMETRIC`；Portal 是一种可见性配置，而不是另一种 `ContainerType`。
### 3. 按顺序提交包内的管线
该包**不会**自动运行。你需要用各自的 `submitBindings` 提交每一条管线，并用 [waitFor](concepts-execution-model#%E7%AE%A1%E7%BA%BF%E6%8E%92%E5%BA%8F) 把它们串联起来，确保 display 阶段能看到 detection 阶段的结果：
```kotlin
var waitFor: Pipeline.RunTask? = initTask
while (isActive) {
    val detectionTask = detection.pipeline.submit(detection.submitBindings, null, waitFor)
    val displayTask   = display.pipeline.submit(display.submitBindings, null, detectionTask)
    waitFor = framePipeline.submit(emptyMap(), null, displayTask)   // feed into next frame
    delay(frameIntervalMs)
}
```

### 4. 需要时传入外部张量
如果你的应用已经拥有一个该包应该使用的张量（例如你自己加载的一个场景），可以在加载时把它通过 `externalGlobals` 传进去，加载器就会绑定这个张量，而不是自行创建一个：
```kotlin
val myScene = session.newSceneFromGLTFSuspend("SpatialML/my_frame.gltf")
val bundle = session.loadPipelinePackageFromAssets(
    "SpatialML/face-mediapipe-pipeline",
    externalGlobals = mapOf("frame_gltf" to myScene),
)
```

## 什么时候应该自己搭建
当没有合适的包可用、你需要更换模型或预处理方式，或者像 [SuperResolution](samples-super-resolution) 和风格化示例那样以自定义方式组合多个模型时，请自己编写图（参见[工作流](workflows-prepare-image-data)和[算子目录](reference-operator-catalog)）。
## 延伸阅读

* [FaceDetection 示例](samples-face-detection)——一个基于管线包构建的完整应用。
* [管线包格式](reference-pipeline-packages)——磁盘上的 manifest / 管线 / 模型 schema。
* [执行模型](concepts-execution-model)——提交、条件与 `waitFor` 排序。

