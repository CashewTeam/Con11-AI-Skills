对两个整型张量执行逐元素按位或运算。可用于在计算图内部合并位掩码或置位。
## 签名
```text
Pipeline.bitwiseOr(
    tensor1: Tensor,
    tensor2: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类别 | 说明 |
| --- | --- | --- |
| `tensor1` | 输入 | 第一个整型张量。 |
| `tensor2` | 输入 | 第二个整型张量（形状需一致）。 |
| `result` | 结果 | 逐元素计算的 `tensor1 \| tensor2`。 |
## 空间模式说明

* 操作数应为整型张量（参见 [Tensor.DataType](zh-reference-tensor-types-and-enums#tensor-datatype)）。
* 可先合并条件掩码，再用 [bytewiseAny](zh-reference-operators-bytewise-any) 进行归约。

## 相关算子

* [bitwiseAnd](zh-reference-operators-bitwise-and) —— 按位与。
* [bytewiseAll](zh-reference-operators-bytewise-all) / [bytewiseAny](zh-reference-operators-bytewise-any) —— 对掩码进行归约。

