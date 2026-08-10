本仓库中的 `SuperResolutionApp` 是参考性的空间模式 SpatialML 应用。它读取头显经过校正的相机画面，裁剪出一个可配置的区域，用端上的 Real-ESRGAN 模型将其放大 4 倍，并把结果显示在一个浮动面板上——这一切都在 SpatialML 运行时内部完成。本页从头到尾走一遍这个应用，并把每个步骤链接到对应的算子和概念页面。
**建议对照源码阅读**
下面每个代码片段都来自 `SuperResolutionApp/src/main/java/com/pico/spatial/ml/sample/sr/`。建议在阅读本页时打开 `vm/SrAlgorithmImpl.kt`——整个算法只用了约 300 行代码。
## 本示例演示了什么

* 在 Android 侧创建 `SpatialMLInstance` 和 `SpatialMLSession`。
* 构建三条协同工作的管线：一条 **init**（初始化）管线、一条逐帧运行的 **main**（主）管线，以及一条按需运行的 **affine**（仿射）管线。
* 两种运行时模式——[安全模式与回读模式](concepts-secure-and-readback-modes)——通过一个布尔值控制同一套代码路径。
* 相机访问、图像预处理、模型推理、动态贴图输出，以及受控的回读。

## 用一个标志位控制两种模式
整个应用都由 `useSecureMr` 这个参数控制：
```kotlin
class SrAlgorithmImpl(
    private val appContext: Context,
    private val scope: CoroutineScope,
    private val useSecureMr: Boolean = false,
)
```

视图模型（view model）会根据用户已确认的选择来决定这个值：
```text
superResolution = SrAlgorithmImpl(
    appContext,
    viewModelScope,
    useSecureMr = appMode.value == AppMode.SECURE_MR_CONFIRMED,
)
```


* **安全模式**（`useSecureMr = true`）：运行时会把结果渲染进一个应用无法读取的容器。会话创建时使用非零的容器尺寸，应用会加载一个 glTF 面板用于显示。
* **回读模式**（`useSecureMr = false`）：允许应用（在拥有相机权限的前提下）把结果回读出来并自行渲染。不会分配容器。

这个开关背后的信任模型请参见[安全模式与回读模式](concepts-secure-and-readback-modes)。
## 步骤 1 — 会话与全局张量
实例创建后会轮询 `ready`，然后打开一个按工作需要设置好大小的会话。容器尺寸只有在安全模式下才为非零：
```kotlin
val session = SpatialMLInstance.create(appContext)
    .also { while (!it.ready) delay(100) }
    .createSession(
        InitInfo(
            imageWidth = CAMERA_IMG_SIZE, imageHeight = CAMERA_IMG_SIZE,   // 512x512
            containerWidth  = if (useSecureMr) 1200 else 0,
            containerHeight = if (useSecureMr) 1200 else 0,
            containerDepth  = if (useSecureMr) 200 else 0,
        )
    )!!
```

那些生命周期长于单次管线运行的全局张量，是在会话上创建的：
```text
if (useSecureMr) {
    displaySceneGraph = session.newSceneFromGLTFSuspend("Display512.glb")   // panel to render into
}
dynamicTexture = session.newGlobalTensor(
    MultiDimensionalInitInfo(
        DataType.Image.R8G8B8A8_U_DYNAMIC,
        intArrayOf(512, 512),
    )
)
zoomAffine = session.newGlobalTensor(
    MultiDimensionalInitInfo(DataType.FLOAT32, intArrayOf(2, 3))            // the crop/zoom matrix
)
```

相关概念：[核心 API](reference-core-api)、[张量与形状](concepts-tensors-and-shapes)、[newSceneFromGLTF](reference-operators-new-scene-from-gltf)。
## 步骤 2 — 初始化管线（仅安全模式）
在安全模式下，应用会把动态贴图一次性地接入面板的材质、将其设为可见并提交——这是一条一次性的设置管线：
```text
session.newPipeline().run {
    updateSceneGraphProperty(displaySceneGraph, "/", PBRMaterials[0].BaseColorTexture, dynamicTexture)
    switchSceneVisibility(displaySceneGraph, displaySceneGraph)
    submit(mapOf(), null, null)
}
```

此后，只要 `dynamicTexture` 发生变化，运行时就会自动重新渲染面板——不需要每帧再做场景图相关的工作。相关算子：[updateSceneGraphProperty](reference-operators-update-scene-graph-property)、[switchSceneVisibility](reference-operators-switch-scene-visibility)、[submit](reference-operators-submit)。
## 步骤 3 — 主管线（逐帧运行）
这是整个应用的核心。它只构建一次，之后持续提交。它读取相机画面、做裁剪/缩放、归一化、运行模型、反归一化，最后写入显示贴图：
```kotlin
// 1. camera in
val rightEyeImg = newLocalTensor(MultiDimensionalInitInfo(DataType.UINT8, intArrayOf(512, 512), 3))
rectifiedVSTAccess(rightImageResult = rightEyeImg, leftImageResult = null,
                   timestampResult = null, cameraMatrixResult = null)

// 2. crop/zoom to model size via the shared affine matrix
val affinedUint8 = newLocalTensor(MultiDimensionalInitInfo(DataType.UINT8, intArrayOf(128, 128), 3))
applyAffine(zoomAffine, rightEyeImg, affinedUint8)

// 3. to float, normalize to 0..1
val affinedFloat = newLocalTensor(MultiDimensionalInitInfo(DataType.FLOAT32, intArrayOf(128, 128), 3))
copy(affinedUint8, affinedFloat)
arithmetic(affinedFloat) { affinedFloat / 255.0 }

// 4. inference
val zoomedResult = newLocalTensor(MultiDimensionalInitInfo(DataType.FLOAT32, intArrayOf(512, 512), 3))
val zoomedResultU8 = newLocalTensor(
    MultiDimensionalInitInfo(DataType.Image.R8G8B8_U, intArrayOf(512, 512))
)
loadAssetToSharedMemory(appContext, "real_esrgan_x4v3.tflite") {
    runModelInference(
        modelName = "real_esrgan_x4v3",
        modelType = Pipeline.ModelInferenceType.LITE_RT_NPU,
        modelBinary = it,
        inputs  = arrayOf(Pipeline.ModelNodeEncoding("image", affinedFloat)),
        outputs = arrayOf(Pipeline.ModelNodeEncoding("upscaled_image", zoomedResult)),
    )
}

// 5. denormalize, convert RGB to RGBA, and publish to the display texture
arithmetic(zoomedResult) { zoomedResult * 255.0 }
copy(zoomedResult, zoomedResultU8)
convertColor(Pipeline.ColorConversion.RGB_TO_RGBA, zoomedResultU8, dynamicTexture)
```

请注意输入/输出张量都是**局部（local）**的——它们只在单次运行中存在——而** **`zoomAffine` 和 `dynamicTexture` 是**全局（global）**的，在各帧之间共享。相关算子：[rectifiedVSTAccess](reference-operators-rectified-vst-access)、[applyAffine](reference-operators-apply-affine)、[copy](reference-operators-copy)、[arithmetic](reference-operators-arithmetic)、[runModelInference](reference-operators-run-model-inference)。相关工作流：[准备图像数据](workflows-prepare-image-data)、[运行模型推理](workflows-run-model-inference)。
RGBA 转换是当前示例渲染路径所需的：实时渲染目标是 `R8G8B8A8_U_DYNAMIC`，因此模型的三通道 RGB 结果首先被转换为 `R8G8B8_U`，然后通过 `ColorConversion.RGB_TO_RGBA` 扩展。这也意味着原始回读数据是每像素四个字节；请拷贝返回的 alpha 字节，而不是自行合成。
## 步骤 4 — 仿射管线（缩放变化时触发）
裁剪区域只会在用户拖动缩放滑块时改变，因此它被放在一条独立的管线中，每次变化时运行一次。它把三个源点写入共享内存，并将计算出的矩阵写入全局的 `zoomAffine` 张量：
```text
getAffine(zoomPoints, targetZoomPoints, zoomAffine)
```

主管线会在下一帧自动拿到新的矩阵，因为两者引用的是同一个全局张量。相关算子：[getAffine](reference-operators-get-affine)。
## 步骤 5 — 驱动各条管线
视图模型通过异步执行器把这三条管线串联起来。仿射更新先运行，随后主管线以 10 Hz 的频率持续运行：
```kotlin
val affineTask = superResolution.setUpscaleFactor(initRatio, superResolution.initTask)
superResolution.mainPipeline.runContinuously(10, affineTask)
```

`AsyncPipelineRunner` 只构建一次图，之后按固定间隔重新提交，用 `waitFor` 把各次运行串联起来，并在放弃之前最多容忍连续 5 次 `SpatialMLException`。参见[异步管线模式](workflows-async-pipeline-patterns)。
## 步骤 6 — 取出结果（回读模式）
在回读模式下，应用会把放大后的图像回读出来——既可以作为纹理资源用于自己的渲染，也可以作为原始字节用于进一步处理（该示例把它发送给了一个 VQA 服务）：
```kotlin
// as a texture resource for a material
fun imageReadbackAsTexture() = scope.async {
    sessionDeferred.await()
    dynamicTexture.readbackAsTextureResourceSuspend()
}

// as raw content (AutoCloseable — copy out, then close promptly)
fun imageReadBack(): Deferred<TensorContent> =
    scope.async { dynamicTexture.readbackContentSuspend() }
```

`TensorContent` 封装了共享内存，必须尽快关闭；该示例在 `use { }` 代码块内把 RGBA 数据拷贝进一个 ARGB 缓冲区。回读只对**全局**张量有效，并且需要相机权限。参见[将数据回读到应用](workflows-read-back-results)。
## 对照表：示例 → 文档
| 示例片段 | 相关文档 |
| --- | --- |
| `SpatialMLInstance` / `createSession` | [核心 API](reference-core-api) |
| `useSecureMr` 分支控制 | [安全模式与回读模式](concepts-secure-and-readback-modes) |
| `rectifiedVSTAccess` | [访问 VST 相机图像](workflows-access-camera-vst) |
| `applyAffine` / `copy` / `arithmetic` | [准备图像数据](workflows-prepare-image-data) |
| `runModelInference` | [运行模型推理](workflows-run-model-inference) |
| `updateSceneGraphProperty` / `switchSceneVisibility` | [驱动场景图输出](workflows-drive-scene-graph-output) |
| `readbackContentSuspend` / `readbackAsTextureResourceSuspend` | [回读数据](workflows-read-back-results) |
| `AsyncPipelineRunner` | [异步管线模式](workflows-async-pipeline-patterns) |
## 延伸阅读

* [第一个 SpatialML 场景](getting-started-first-spatialml-scene)——自己动手搭建一个最小版本。
* [算子目录](reference-operator-catalog)——本示例用到的所有算子，以及更多。
* [疑难排查](troubleshooting)——当管线悄无声息地不产生任何结果时怎么办。

