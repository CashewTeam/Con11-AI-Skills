按照 [NormalizeType](zh-reference-tensor-types-and-enums#%E9%A2%9C%E8%89%B2-%E5%BD%92%E4%B8%80%E5%8C%96-%E8%8C%83%E6%95%B0%E4%B8%8E%E6%8E%92%E5%BA%8F%E7%9B%B8%E5%85%B3%E6%9E%9A%E4%B8%BE)（例如最小-最大缩放或均值/标准差归一化）对张量的数值进行归一化。用它可以把图像或特征数据变换到模型所期望的数值范围。
## 签名
```text
Pipeline.normalize(
    type: NormalizeType,
    source: Tensor,
    alphaBeta: Tensor?,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `type` | enum | 要应用的归一化方案——`L1`、`L2`、`INF` 或 `MINMAX`。 |
| `source` | 输入 | 要归一化的张量。必须是多维张量。 |
| `alphaBeta` | 输入 | 可选的双值张量，用于提供缩放参数（例如 `MINMAX` 的最小/最大范围）。传入 `null` 则使用默认值。 |
| `result` | 结果 | 归一化后的张量。必须与 `source` 具有相同的 `InitInfo`。 |
## 空间模式说明

* 预置的归一化方案通常比手写数学表达式更简洁；SuperResolutionApp 使用简单的 `arithmetic(t) { t / 255.0 }`，是因为它的方案很简单，但带有均值/标准差预处理的模型自然更适合用 `normalize`。
* 务必让方案与模型训练时的预处理完全匹配。

## 相关算子

* [arithmetic](zh-reference-operators-arithmetic) —— 自定义缩放表达式。
* [norm](zh-reference-operators-norm) —— 度量幅值（不做缩放）。
* [为模型准备图像数据](zh-workflows-prepare-image-data)

