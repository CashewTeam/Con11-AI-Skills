逐元素“小于等于”比较（`tensor1 <= tensor2`），将布尔式结果写入结果张量。
## 签名
```text
Pipeline.smallerEqual(
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
| `result` | 结果 | `tensor1 <= tensor2` 处为非零。 |
## 空间模式说明

* 操作数的形状必须兼容。
* 如需单一的条件值，可用 [bytewiseAll](zh-reference-operators-bytewise-all) / [bytewiseAny](zh-reference-operators-bytewise-any) 进行归约。

## 相关算子

* [smallerThan](zh-reference-operators-smaller-than) —— 严格小于变体。
* [largerThan](zh-reference-operators-larger-than) / [largerEqual](zh-reference-operators-larger-equal) —— 相反方向。

