计算张量的向量范数或矩阵范数，按照 [NormType](zh-reference-tensor-types-and-enums#%E9%A2%9C%E8%89%B2-%E5%BD%92%E4%B8%80%E5%8C%96-%E8%8C%83%E6%95%B0%E4%B8%8E%E6%8E%92%E5%BA%8F%E7%9B%B8%E5%85%B3%E6%9E%9A%E4%B8%BE)（例如 L1、L2 或无穷范数）将其归约为一个幅值。
## 签名
```text
Pipeline.norm(
    type: NormType,
    srcTensor: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `type` | enum | 要计算的范数类型——`L1`、`L2` 或 `INF`。 |
| `srcTensor` | 输入 | 要度量的张量。 |
| `result` | 结果 | 接收范数结果的标量（或降维后的）张量。 |
## 空间模式说明

* 用于在计算图内部度量距离或幅值（例如关键点之间的向量长度）。
* 若要将张量缩放到单位范围，请优先使用 [normalize](zh-reference-operators-normalize)；`norm` 只做度量。

## 相关算子

* [normalize](zh-reference-operators-normalize) —— 重新缩放数值。
* [arithmetic](zh-reference-operators-arithmetic) —— 将测得的范数用于进一步的数学运算。

