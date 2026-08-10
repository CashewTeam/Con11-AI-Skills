大多数 SpatialML 管线都从透视（VST）相机开始。[rectifiedVSTAccess](reference-operators-rectified-vst-access) 算子会把一帧经过校正的立体图像连同其时间戳和相机内参一起拉取到图中。本页介绍如何使用它，以及图像尺寸与你的会话之间的关系。
## 能拿到什么
`rectifiedVSTAccess` 最多写入四个结果张量，每个都是可选的——不需要的传 `null` 即可：
| 结果 | 张量形状 | 类型 | 用途 |
| --- | --- | --- | --- |
| `rightImageResult` | `(H, W)`，3 通道 | `UINT8` RGB | 右眼校正图像 |
| `leftImageResult` | `(H, W)`，3 通道 | `UINT8` RGB | 左眼校正图像 |
| `timestampResult` | 时间戳张量 | `INT32`，4 通道 | 在时间上关联该帧 |
| `cameraMatrixResult` | `(3, 3)` | `FLOAT32` | 用于[2D→3D 投影](reference-operators-uv-to-3d-in-camera-space)的内参 |
请把同一次调用得到的结果放在一起使用——它们描述的是同一帧连贯的数据。
## 最小用法
先创建结果张量，再调用该算子。示例只需要右眼图像：
```kotlin
val rightEye = newLocalTensor(
    MultiDimensionalInitInfo(DataType.UINT8, intArrayOf(512, 512), channel = 3)
)
rectifiedVSTAccess(
    rightImageResult = rightEye,
    leftImageResult = null,
    timestampResult = null,
    cameraMatrixResult = null,
)
```

## 让尺寸匹配会话的图像大小
运行时会按你在 [InitInfo](reference-core-api#spatialmlsession) 中声明的尺寸提供图像帧：
```text
createSession(InitInfo(imageWidth = 512, imageHeight = 512, /* ... */))
```

把图像结果张量分配为相同的尺寸（`intArrayOf(512, 512)`）可以避免每帧都做一次缩放。如果绑定的张量尺寸不同，运行时会把数据缩放进去，每帧都多一份开销。
**图像张量的形状**
图像张量的形状是 `intArrayOf(height, width)`，像素分量由 `channel` 表示。一帧 512×512 的 RGB 图像对应 `intArrayOf(512, 512)`，`channel = 3`。参见[张量与形状](concepts-tensors-and-shapes)。
## 典型的后续步骤

* 为模型预处理图像——[为模型准备图像数据](workflows-prepare-image-data)。
* 把检测结果转换为 3D 放置信息——[uvTo3DInCameraSpace](reference-operators-uv-to-3d-in-camera-space)。
* 需要深度而不是颜色——[getDepthMap](reference-operators-get-depth-map)。

## 权限
在图内部访问 VST 本身**并不**需要相机权限——在 [安全模式](concepts-secure-and-readback-modes)下，像素数据永远不会离开运行时。只有当你之后要把处理结果[回读](workflows-read-back-results)到应用代码中时（[回读模式](concepts-secure-and-readback-modes)），才需要 `CAMERA` 权限。
## 延伸阅读

* [rectifiedVSTAccess](reference-operators-rectified-vst-access)[ 算子卡片](reference-operators-rectified-vst-access)
* [为模型准备图像数据](workflows-prepare-image-data)
* [getDepthMap](reference-operators-get-depth-map)[ 算子卡片](reference-operators-get-depth-map)

