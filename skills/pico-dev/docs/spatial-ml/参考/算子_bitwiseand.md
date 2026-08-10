对两个整型张量执行逐元素按位与运算。可用于在计算图内部合并位掩码或清除某些位。
## 签名
```text
Pipeline.bitwiseAnd(
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
| `result` | 结果 | 逐元素计算的 `tensor1 & tensor2`。 |
## 空间模式说明

* 操作数应为整型张量（参见 [Tensor.DataType](zh-reference-tensor-types-and-enums#tensor-datatype)）。
* 常与比较掩码搭配使用：先对两个条件掩码做 AND 运算，再用 [bytewiseAll](zh-reference-operators-bytewise-all) 进行归约。

## 相关算子

* [bitwiseOr](zh-reference-operators-bitwise-or) —— 按位或。
* [bytewiseAll](zh-reference-operators-bytewise-all) / [bytewiseAny](zh-reference-operators-bytewise-any) —— 对掩码进行归约。

