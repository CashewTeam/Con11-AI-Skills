取两个张量的逐元素最大值，将每个位置上较大的值写入结果张量。适合用于下限截断（例如针对常量张量做类似 ReLU 的下限处理）或合并两张候选图。
## 签名
```text
Pipeline.elementwiseMax(
    tensor1: Tensor,
    tensor2: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类别 | 说明 |
| --- | --- | --- |
| `tensor1` | 输入 | 第一个张量。 |
| `tensor2` | 输入 | 第二个张量（形状需一致）。 |
| `result` | 结果 | 逐元素最大值。 |
## 空间模式说明

* 操作数的形状必须兼容。
* 可与 [elementwiseMin](zh-reference-operators-elementwise-min) 搭配使用，将数值截断到某个范围内。

## 相关算子

* [elementwiseMin](zh-reference-operators-elementwise-min) —— 逐元素最小值。
* [elementwiseMultiply](zh-reference-operators-elementwise-multiply) —— 逐元素乘积。
* [arithmetic](zh-reference-operators-arithmetic) —— 表达式运算。

