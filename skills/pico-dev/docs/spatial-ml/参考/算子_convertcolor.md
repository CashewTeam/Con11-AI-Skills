按照 [ColorConversion](zh-reference-tensor-types-and-enums#%E9%A2%9C%E8%89%B2-%E5%BD%92%E4%B8%80%E5%8C%96-%E8%8C%83%E6%95%B0%E4%B8%8E%E6%8E%92%E5%BA%8F%E7%9B%B8%E5%85%B3%E6%9E%9A%E4%B8%BE) 代码，在不同的颜色排布和通道数之间转换图像张量（例如 RGB ↔ BGR、RGB → 灰度，或添加/移除 alpha 通道）。
## 签名
```text
Pipeline.convertColor(
    conversionType: ColorConversion,
    source: Tensor,
    result: Tensor,
)

// OpenCV-style string overload (e.g. "COLOR_RGB2GRAY")
Pipeline.convertColor(
    opencvConvertStr: String,
    source: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类别 | 说明 |
| --- | --- | --- |
| `conversionType` | 枚举 | 要应用的 [ColorConversion](zh-reference-tensor-types-and-enums#%E9%A2%9C%E8%89%B2-%E5%BD%92%E4%B8%80%E5%8C%96-%E8%8C%83%E6%95%B0%E4%B8%8E%E6%8E%92%E5%BA%8F%E7%9B%B8%E5%85%B3%E6%9E%9A%E4%B8%BE)。源张量的通道数必须与该转换所要求的输入通道数一致。 |
| `opencvConvertStr` | 字符串 | `conversionType` 的替代方式：一个 OpenCV 转换名称。 |
| `source` | 输入 | 源图像张量。 |
| `result` | 结果 | 目标图像张量；其通道数必须与目标格式一致。 |
## 空间模式说明

* 按转换后产生的通道数分配 `result`（例如灰度图 `channel = 1`，RGB/BGR 为 `3`）。`result` 的维度必须与 `source` 相同。
* 请确保颜色排布与模型训练时使用的一致——这里的不匹配是导致推理结果异常的常见原因。
* 如需纯数值类型转换（UINT8 → FLOAT32），请使用 [copy](zh-reference-operators-copy)；如需数值范围缩放，请使用 [arithmetic](zh-reference-operators-arithmetic) 或 [normalize](zh-reference-operators-normalize)。

## 相关算子

* [copy](zh-reference-operators-copy) —— 数据类型转换。
* [normalize](zh-reference-operators-normalize) —— 数值范围归一化。
* [switchCHWAndHWC](zh-reference-operators-switch-chw-and-hwc) —— 更改维度顺序。
* [为模型准备图像数据](zh-workflows-prepare-image-data)

