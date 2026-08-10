将数据从源张量复制到目标张量。当两个张量的[数据类型](reference-tensor-types-and-enums#tensor-datatype)不同时，数值会被自动转换——这是将 `UINT8` 像素转换为 `FLOAT32` 模型输入的惯用方式。
## 签名
```text
Pipeline.copy(src: Tensor, dst: Tensor)
```

`copy` 针对不同的源/目标张量种类提供了多个重载。
## 参数
| 参数 | 说明 |
| --- | --- |
| `src` | 源张量。 |
| `dst` | 目标张量；接收（可能经过类型转换的）数据。 |
## 示例
以下摘自 SuperResolutionApp——两次类型转换后进行 RGBA 纹理写入：
```text
// UINT8 -> FLOAT32 conversion by copying between different-typed tensors
copy(affinedUint8, affinedFloat)

// FLOAT32 RGB -> UINT8 RGB, then convert into the RGBA dynamic display texture
copy(zoomedResult, zoomedResultU8)
convertColor(Pipeline.ColorConversion.RGB_TO_RGBA, zoomedResultU8, dynamicTexture)
```

## 空间模式说明

* 更新[动态纹理](concepts-tensors-and-shapes#%E5%8A%A8%E6%80%81%E7%BA%B9%E7%90%86)全局张量就是逐帧计算图更新可见输出的方式（运行时会自动重新渲染）。对于当前的 8 位色彩渲染路径，请使用 [convertColor](reference-operators-convert-color) 将 RGB 转换为 `R8G8B8A8_U_DYNAMIC` 目标。
* 源张量与目标张量的形状必须兼容。

## 相关算子

* [arithmetic](reference-operators-arithmetic) —— 在单个表达式中同时完成复制与缩放。
* [convertColor](reference-operators-convert-color) —— 更改颜色排布，而不仅仅是类型。
* [为模型准备图像数据](workflows-prepare-image-data)

