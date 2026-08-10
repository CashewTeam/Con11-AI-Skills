SpatialML 的图会"悄无声息"地失败：因为算子只*描述*要做的工作，真正的执行发生在运行时中，所以出错时通常表现为面板空白或回读结果全是零，而不是抛出异常。本页按大致出现频率列出你实际会遇到的失败模式，以及应该具体检查什么。
## 会话始终无法就绪
**症状：**`SpatialMLInstance.create(...)` 已返回，但 `.ready` 一直是 `false`，或者 `createSession(...)` 返回 `null`。

* 确认你运行在受支持的 PICO 设备（或 PICO 模拟器）上，并且已具备 Spatial SDK 运行时。SpatialML 无法在编辑器中运行。
* 检查[前置条件](getting-started-prerequisites)中提到的 manifest 标志位和权限是否齐全。
* 在主线程之外轮询 `ready`（示例中使用了带 `delay(100)` 的协程）；如果在主线程上阻塞等待，会在其变为 true 之前就先触发 ANR。

## 安全模式下面板空白
**症状：**一切运行都没有报错，但显示面板什么都不显示。

* 你在 `InitInfo` 中分配了**非零的容器**吗？安全模式需要 `containerWidth/Height/Depth > 0`。示例中使用的是 `1200 × 1200 × 200`。
* **初始化管线**运行了吗？贴图/材质绑定和 `switchSceneVisibility` 必须在逐帧循环开始之前提交一次。
* 渲染目标是动态纹理吗？对于 8 位色彩输出，请使用 `DataType.Image.R8G8B8A8_U_DYNAMIC`。
* 你的管线产生的是 RGB 吗？请用 `convertColor(ColorConversion.RGB_TO_RGBA, rgbOutput, dynamicTexture)` 将其转换为 RGBA 渲染目标。三通道 RGB 动态纹理可能在渲染路径上失败。
* 实体路径对不对？示例绑定在 `"/"`（根节点）上；路径写错会悄无声息地不产生任何效果。参见 [updateSceneGraphProperty](reference-operators-update-scene-graph-property)。

## 被追踪内容在容器边缘消失
**症状：**检测或追踪仍在继续，但当目标移得更远或移出配置的体积时，`CameraAnchor.Follow` 实体消失了。

* 常规 `VOLUMETRIC` SpatialML 容器会在其边界处裁剪内容。即使相机空间变换仍然有效，这也是预期行为。
* 如果内容必须在该盒子之外保持可见，请用 `SpatialMLSession.InitInfo(...).addPortal()` 配置会话。portal 通过背面面板暴露超出边界的内容。
* `addPortal()` 要求 `ContainerType.VOLUMETRIC` 且宽、高、深均为正值；对 `PLANAR`、`DISABLED` 或非正尺寸会抛出异常。
* portal 本身不执行锚定。请继续用被追踪的变换更新 `SceneGraphProperty.CameraAnchor.Follow`。

参见[容器与传送门](concepts-containers-and-portals)了解与常规 Volume 的比较。
## 回读结果全是零
**症状：**`readbackContent()` / `readbackAsTextureResource()` 返回一个全是零的缓冲区。

* 回读只对**全局**张量有效。局部张量的数据在本次运行结束后就不再存在——你无法把它回读出来。请先把结果拷贝进一个全局张量。
* 确保填充该张量的管线在你读取之前确实**已经运行并完成**。可以等待 `RunTask`，或使用异步执行器的排序机制（`waitFor`）。
* 在回读模式下，拉取结果需要相机权限——没有权限时回读会被阻止。参见[回读数据](workflows-read-back-results)。
* 及时关闭 `TensorContent`（它封装了共享内存）；读取一个过期/已关闭的 content 是一种常见的、自己制造出来的"全零"问题。

## 模拟器上什么都检测不到 / 结果为空
**症状：**图运行没有报错，但相机或深度驱动的阶段什么都不产生——空白帧、全零的检测结果、没有 3D 放置。

* **PICO 模拟器**支持 SpatialML，但没有真实的透视相机、深度传感器或麦克风。传感器类算子——[rectifiedVSTAccess](reference-operators-rectified-vst-access)、[getDepthMap](reference-operators-get-depth-map)、[captureMicrophone](reference-operators-capture-microphone)——以及依赖它们的任何算子（例如 [uvTo3DInCameraSpace](reference-operators-uv-to-3d-in-camera-space)）在模拟器上都无法返回真实数据。
* 相机驱动的功能，包括像 [FaceDetection](samples-face-detection) 这样的 [Pipeline Zoo](workflows-use-pipeline-packages) 包，都需要真机才能产出结果。可以用模拟器验证接线和图结构是否正确，但行为验证要在真机上进行。参见[在模拟器上运行](getting-started-prerequisites#%E5%9C%A8%E6%A8%A1%E6%8B%9F%E5%99%A8%E4%B8%8A%E8%BF%90%E8%A1%8C)。

## 模型推理结果是乱码
**症状：**模型运行了，但输出是噪声或不正确。

* **归一化不匹配：**喂给模型的数据范围必须与训练时完全一致。示例在推理前做了 `{ t / 255.0 }`，推理后做了 `{ t * 255.0 }`——参见 [arithmetic](reference-operators-arithmetic) 和 [normalize](reference-operators-normalize)。
* **节点名称：**`ModelNodeEncoding` 的 `nodeName` 必须与模型真实的输入/输出节点名称一致（示例中是 `"image"`、`"upscaled_image"`），而不是你以为它应该叫的名字。
* **形状/类型：**输出张量必须预先按模型精确的输出形状和 `DataType` 分配好。
* **数据排布：**如果模型期望 CHW 但你给的是 HWC（或反过来），需要插入 [switchCHWAndHWC](reference-operators-switch-chw-and-hwc)。
* **后端：**模型二进制文件必须是 TensorFlow Lite FlatBuffer（`.tflite`）；`ModelInferenceType` 只用于选择加速器（`LITE_RT_CPU`/`LITE_RT_GPU`/`LITE_RT_NPU`）。如果某个加速器跑不了某个算子，可以换一个试试（例如从 `LITE_RT_NPU` 降级到 `LITE_RT_GPU`）。参见 [runModelInference](reference-operators-run-model-inference)。

## `arithmetic` 抛出异常或不执行任何操作

* `arithmetic` 只支持**多维**张量（[MultiDimensionalInitInfo](reference-tensor-types-and-enums#multidimensionalinitinfo)）。标量/数组类型的 init-info 张量不是合法的操作数。
* 所有操作数都必须是**二维浮点**矩阵，且一个闭包最多只能引用 10 个张量。请先用 [copy](reference-operators-copy) 把 `UINT8` 图像数据转换成浮点张量，并把过长的表达式拆分到多次 `arithmetic` 调用中。

## 管线提交一直失败
**症状：**Logcat 中反复出现 `pipeline submit fail due to exception`。

* 异步执行器最多容忍**连续 5 次** `SpatialMLException`，之后会停止循环（参见[异步管线模式](workflows-async-pipeline-patterns)）。如果你的循环挂掉了，要找的是第一次异常，而不是最后一次。
* 一条管线如果要消费另一条管线的输出，必须用 `waitFor` 排好顺序——否则它会读到一个尚未被填充的张量。参见 [submit](reference-operators-submit)。
* 每帧都重新构建图、而不是重新提交一条已经构建好的管线，既慢又容易产生竞态。应该只构建一次，多次提交。

## 图像方向或尺寸不对

* [applyAffine](reference-operators-apply-affine) 的**目标**张量决定了输出分辨率——应该按模型的输入尺寸来分配它，而不是相机的尺寸。
* 图像类 init-info 的 dimensions 是 `intArrayOf(height, width)`，通道数单独用 `channel` 指定；把高和宽写反是一个常见的错误。参见[张量与形状](concepts-tensors-and-shapes)。

## 应用启动时卡死 / ANR

* 原生模型初始化和实例就绪检测不能放在主线程上执行。应该在后台调度器的协程中做会话初始化和 `loadAssetToSharedMemory`。

## 仍未解决？

* 重新阅读[运行时模型](concepts-mental-model)——大多数"悄无声息"的问题都是把*描述*和*执行*、或者*局部*和*全局*张量搞混了导致的。
* 对照[SuperResolutionApp 演练](samples-super-resolution)看看；它端到端地演练了每一条算子路径。
* 在 logcat 中搜索 `"SpatialML"` 标签——示例在设置和提交的每个阶段都打了日志。

