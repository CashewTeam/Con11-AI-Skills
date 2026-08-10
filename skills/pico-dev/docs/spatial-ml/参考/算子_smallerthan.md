逐元素严格小于比较（`tensor1 < tensor2`），将布尔风格的结果写入结果张量。
## 签名
```text
Pipeline.smallerThan(
    tensor1: Tensor,
    tensor2: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `tensor1` | 输入 | 左侧张量。 |
| `tensor2` | 输入 | 右侧张量（形状需匹配）。 |
| `result` | 结果 | 在 `tensor1 < tensor2` 处为非零值。 |
## 空间模式说明

* 操作数形状必须兼容。
* 可用于阈值判断，再通过 [bytewiseAny](zh-reference-operators-bytewise-any) / [bytewiseAll](zh-reference-operators-bytewise-all) 进行归约。

## 相关算子

* [smallerEqual](zh-reference-operators-smaller-equal) —— 包含相等的变体。
* [largerThan](zh-reference-operators-larger-than) / [largerEqual](zh-reference-operators-larger-equal) —— 方向相反的比较。

