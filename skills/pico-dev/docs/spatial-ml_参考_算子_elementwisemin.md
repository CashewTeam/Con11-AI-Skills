对两个张量取逐元素最小值，将每个位置上较小的值写入结果张量。可用于向上限幅或合并候选图。
## 签名
```text
Pipeline.elementwiseMin(
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
| `result` | 结果 | 逐元素最小值。 |
## 空间模式说明

* 操作数的形状必须兼容。
* 可与 [elementwiseMax](zh-reference-operators-elementwise-max) 搭配使用，将数值限制在某个范围内。

## 相关算子

* [elementwiseMax](zh-reference-operators-elementwise-max) — 逐元素取最大值。
* [elementwiseMultiply](zh-reference-operators-elementwise-multiply) — 逐元素相乘。
* [arithmetic](zh-reference-operators-arithmetic) — 表达式运算。

