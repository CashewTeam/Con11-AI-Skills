对两个张量执行逐元素相等性比较，将布尔风格的结果（相等处为非零值）写入结果张量。
## 签名
```text
Pipeline.equal(
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
| `result` | 结果 | 在 `tensor1 == tensor2` 处为非零值。 |
## 空间模式说明

* 操作数的形状必须兼容。
* 可与 [bytewiseAll](zh-reference-operators-bytewise-all) / [bytewiseAny](zh-reference-operators-bytewise-any) 结合使用，将掩膜归约为单一条件，例如作为 [submit](zh-reference-operators-submit) 的条件张量。

## 相关算子

* [notEqual](zh-reference-operators-not-equal) — 相反的比较测试。
* [largerThan](zh-reference-operators-larger-than) / [smallerThan](zh-reference-operators-smaller-than) — 大小顺序比较。
* [bytewiseAll](zh-reference-operators-bytewise-all) / [bytewiseAny](zh-reference-operators-bytewise-any) — 归约掩膜。

