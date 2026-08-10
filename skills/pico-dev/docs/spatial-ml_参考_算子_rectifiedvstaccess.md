提供经过校正的左眼和右眼 VST 图像，并附带匹配的相机时间戳与内参矩阵。它通常是相机驱动型管线的起点。
## 签名
```text
Pipeline.rectifiedVSTAccess(
    rightImageResult: Tensor?,
    leftImageResult: Tensor?,
    timestampResult: Tensor?,
    cameraMatrixResult: Tensor?,
)
```

## 参数 / 结果
每个参数都是一个由你分配并传入的**结果**张量。对于不需要的项传入 `null` 即可。
| 参数 | 张量形状 | 类型 | 说明 |
| --- | --- | --- | --- |
| `rightImageResult` | `(H, W)`，3 通道 | `UINT8` RGB | 校正后的右眼 VST 图像。 |
| `leftImageResult` | `(H, W)`，3 通道 | `UINT8` RGB | 校正后的左眼 VST 图像。 |
| `timestampResult` | 时间戳张量 | `INT32`，4 通道 | 该帧的相机时间戳。 |
| `cameraMatrixResult` | `(3, 3)` | `FLOAT32` | 该帧的相机内参矩阵。 |
将图像结果的尺寸与 session 的 [InitInfo](zh-reference-core-api#spatialmlsession) 中 `imageWidth`/`imageHeight` 保持一致，以避免逐帧缩放。
## 示例
来自 SuperResolutionApp——只需要右眼图像：
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

## 空间模式说明

* 没有配置项，也没有操作数——它只产生结果。
* 请将同一次调用产生的结果放在一起使用；它们描述的是同一帧、彼此一致的数据。
* 在 [Secure Mode](zh-concepts-secure-and-readback-modes) 下，在计算图内部访问 VST 无需相机权限；只有在[将处理后的结果回读](zh-workflows-read-back-results)时才需要权限。

## 相关算子

* [getDepthMap](zh-reference-operators-get-depth-map) —— 获取深度而非颜色。
* [applyAffine](zh-reference-operators-apply-affine) / [getAffine](zh-reference-operators-get-affine) —— 对图像做预处理。
* [uvTo3DInCameraSpace](zh-reference-operators-uv-to-3d-in-camera-space) —— 将检测结果投影到 3D。
* [访问 VST 相机图像](zh-workflows-access-camera-vst)

