通过 2×3 仿射矩阵对源图像进行重采样，并将变形后的结果写入目标图像张量。它是将相机帧裁剪、缩放到模型所需输入尺寸的主力算子。
## 签名
```text
Pipeline.applyAffine(
    affineMatrix: Tensor,
    srcImage: Tensor,
    affinedImage: Tensor,
)
```

## 参数 / 结果
| 名称 | 类别 | 说明 |
| --- | --- | --- |
| `affineMatrix` | 输入 | `FLOAT32` `[2, 3]` 矩阵，通常来自 [getAffine](zh-reference-operators-get-affine)。 |
| `srcImage` | 输入 | 源图像张量。 |
| `affinedImage` | 结果 | 目标图像张量；其形状决定输出尺寸。 |
## 示例
以下摘自 SuperResolutionApp——将校正后的相机图像裁剪/缩放为模型的输入分辨率：
```kotlin
val rightEyeImg  = newLocalTensor(MultiDimensionalInitInfo(DataType.UINT8, intArrayOf(512, 512), 3))
val affinedUint8 = newLocalTensor(MultiDimensionalInitInfo(DataType.UINT8, intArrayOf(128, 128), 3))

rectifiedVSTAccess(rightImageResult = rightEyeImg, /* ... */)
applyAffine(zoomAffine, rightEyeImg, affinedUint8)   // 512x512 -> 128x128 crop
```

## 空间模式说明

* **目标**张量的维度决定输出分辨率——请按模型所需的尺寸分配它。
* 源图像与目标图像的通道数必须一致。
* 可与 [copy](zh-reference-operators-copy) 及 [arithmetic](zh-reference-operators-arithmetic) 搭配使用，将数据类型和数值范围转换为模型所需的数值范围。

## 相关算子

* [getAffine](zh-reference-operators-get-affine) —— 生成本算子所使用的矩阵。
* [applyAffinePoint](zh-reference-operators-apply-affine-point) —— 变换点而非像素。
* [convertColor](zh-reference-operators-convert-color) —— 更改通道排布。
* [为模型准备图像数据](zh-workflows-prepare-image-data)

