本教程搭建一个最小的、可用的 SpatialML 图：访问相机、应用一个简单的变换，并将结果展示在[安全模式](concepts-secure-and-readback-modes)场景中。它只使用 Pipeline 算子和核心 API，因此你可以在添加模型之前先确认项目的接线是否正确。它的结构对应 [SuperResolutionApp](samples-super-resolution) 去掉模型步骤后的样子。
**开始之前**
请先完成[前置条件](getting-started-prerequisites)，并浏览一遍[运行时模型](concepts-mental-model)。这个场景要读取透视相机画面，因此请在真实的 PICO 设备上运行以查看真实输出——[模拟器](getting-started-prerequisites#%E5%9C%A8%E6%A8%A1%E6%8B%9F%E5%99%A8%E4%B8%8A%E8%BF%90%E8%A1%8C)可以运行 SpatialML，但无法提供实时相机图像。
## 1. 创建实例与会话
一切都从一个 [SpatialMLInstance](reference-core-api#spatialmlinstance) 开始。创建过程是异步的：使用前先轮询 `ready`，然后打开一个[会话](reference-core-api#spatialmlsession)。请在主线程之外执行这一步——示例代码中使用的是协程。
```kotlin
private val sessionDeferred = scope.async {
    val session = SpatialMLInstance.create(appContext)
        .also {
            while (!it.ready) delay(100)          // wait until the runtime is up
            Log.i("SpatialML", "SpatialMLInstance ready")
        }
        .createSession(
            InitInfo(
                imageWidth = 512, imageHeight = 512,   // VST image size
                containerWidth = 1200,                 // Secure Mode: non-zero container
                containerHeight = 1200,
                containerDepth = 200,
            )
        )!!
    session
}
```

`InitInfo` 声明了运行时应提供的相机图像尺寸，以及运行时所拥有场景的容器体积。在[回读模式](concepts-secure-and-readback-modes)下，容器尺寸为 `0`。
本教程使用常规的[立体容器](concepts-containers-and-portals)，它会在盒子边界处裁剪内容。如果你的场景将使用 `CameraAnchor.Follow` 来追踪一个可能移出该盒子的对象，请在 `InitInfo` 上链式调用 `.addPortal()`；参见[容器与传送门](concepts-containers-and-portals#%E5%B8%B8%E8%A7%84-volume-%E4%B8%8E-portal)。
## 2. 创建会话范围的张量与场景
创建图将要写入的持久化数据，并加载运行时要渲染的场景。这些都是[全局张量](concepts-tensors-and-shapes#%E5%85%A8%E5%B1%80%E5%BC%A0%E9%87%8F%E4%B8%8E%E6%9C%AC%E5%9C%B0%E5%BC%A0%E9%87%8F)——它们的生命周期超越任何单次管线运行。
```kotlin
// a live texture the runtime can render (image output of the graph)
val dynamicTexture = session.newGlobalTensor(
    MultiDimensionalInitInfo(
        DataType.Image.R8G8B8A8_U_DYNAMIC,
        intArrayOf(512, 512),
    )
)

// a scene loaded from a glTF asset (Secure Mode display surface)
val displayScene = session.newSceneFromGLTFSuspend("Display512.glb")
```

## 3. 搭建初始化管线（一次性接好输出）
有些工作只需要执行一次：把动态纹理绑定到场景的材质中，并让场景可见。把它放在一个专门的初始化管线中完成。这些都是一次性的[场景图算子](workflows-drive-scene-graph-output)。
```text
session.newPipeline().run {
    updateSceneGraphProperty(
        displayScene, "/", PBRMaterials[0].BaseColorTexture, dynamicTexture,
    )
    switchSceneVisibility(displayScene, displayScene)
    submit(mapOf(), null, null)          // run once
}
```

## 4. 搭建逐帧管线
这个图每帧都会运行：获取右眼 VST 图像，并将其拷贝到动态纹理中。（在真实应用中，你会在这些步骤之间加入预处理并运行一个模型——参见[运行模型推理](workflows-run-model-inference)。）
```kotlin
session.newPipeline().apply {
    val rightEye = newLocalTensor(
        MultiDimensionalInitInfo(DataType.UINT8, intArrayOf(512, 512), channel = 3)
    )
    rectifiedVSTAccess(
        rightImageResult = rightEye,
        leftImageResult = null,
        timestampResult = null,
        cameraMatrixResult = null,
    )
    // Dynamic render textures use RGBA. Convert the RGB camera image before publishing it.
    convertColor(Pipeline.ColorConversion.RGB_TO_RGBA, rightEye, dynamicTexture)
}
```

## 5. 提交——初始化一次，逐帧持续提交
顺序很重要：初始化管线必须在逐帧循环之前运行，这样纹理才能在运行时渲染它之前完成绑定。用 [waitFor](concepts-execution-model#%E7%AE%A1%E7%BA%BF%E6%8E%92%E5%BA%8F) 把它们串联起来。
```kotlin
val initTask = initPipeline.submit(mapOf(), null, null)

// submit the per-frame pipeline repeatedly, after init completes
scope.launch {
    var task: Pipeline.RunTask? = initTask
    while (isActive) {
        framePipeline.submit(mapOf(), null, task)
        task = null
        delay(100)   // ~10 Hz
    }
}
```

在生产环境中，请使用示例代码里的 [AsyncPipelineRunner](workflows-async-pipeline-patterns)，它在这个循环外面包装了失败处理和张量映射更新逻辑。
## 6. 运行并验证

1. 部署到设备上，并启动进入空间 shell。
2. 按 `SpatialML` 过滤 logcat；你应该能看到 "ready"、场景已加载以及提交相关的日志。
3. `Display512` 面板应显示实时（未经处理）的相机图像。

如果面板是空白的，检查初始化管线是否在逐帧循环之前运行，以及动态纹理的尺寸是否与场景材质匹配。参见[疑难排查](troubleshooting)。
## 接下来做什么

* [访问 VST 相机图像](workflows-access-camera-vst) —— 深入了解相机数据。
* [为模型准备图像数据](workflows-prepare-image-data) —— 裁剪、缩放、归一化。
* [运行模型推理](workflows-run-model-inference) —— 给图添加一个模型。
* [SuperResolutionApp](samples-super-resolution) —— 本教程所基于的完整示例。

