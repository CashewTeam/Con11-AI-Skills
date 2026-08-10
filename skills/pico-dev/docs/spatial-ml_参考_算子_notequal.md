对两个张量进行逐元素不等性判断，将布尔式结果（数值不同处为非零）写入结果张量。
## 签名
```text
Pipeline.notEqual(
    tensor1: Tensor,
    tensor2: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `tensor1` | 输入 | 第一个张量。 |
| `tensor2` | 输入 | 第二个张量（形状需匹配）。 |
| `result` | 结果 | `tensor1 != tensor2` 处为非零。 |
## 空间模式说明

* 操作数的形状必须兼容。
* 当需要单一的条件值时，可用 [bytewiseAll](zh-reference-operators-bytewise-all) / [bytewiseAny](zh-reference-operators-bytewise-any) 对结果掩码进行归约。

## 相关算子

* [equal](zh-reference-operators-equal) —— 相反的判断。
* [bytewiseAll](zh-reference-operators-bytewise-all) / [bytewiseAny](zh-reference-operators-bytewise-any) —— 归约掩码。

