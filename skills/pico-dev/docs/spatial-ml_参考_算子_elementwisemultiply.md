逐元素相乘两个张量，将乘积写入结果张量。可用于掩膜（masking）、增益图，或每个位置需要独立缩放的哈达玛积（Hadamard product）场景。
## 签名
```text
Pipeline.elementwiseMultiply(
    tensor1: Tensor,
    tensor2: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `tensor1` | 输入 | 第一个张量。 |
| `tensor2` | 输入 | 第二个张量（形状需匹配）。 |
| `result` | 结果 | 逐元素乘积。 |
## 空间模式说明

* 操作数的形状必须兼容。
* 如需使用标量的表达式风格运算（例如 `{ t * 255.0 }`），请改用 [arithmetic](zh-reference-operators-arithmetic)；本算子用于两个完整张量之间的运算。

## 相关算子

* [arithmetic](zh-reference-operators-arithmetic) — 表达式运算。
* [elementwiseMax](zh-reference-operators-elementwise-max) / [elementwiseMin](zh-reference-operators-elementwise-min)

