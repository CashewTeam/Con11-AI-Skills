逐元素执行严格大于比较（`tensor1 > tensor2`），将布尔风格的结果写入结果张量。
## 签名
```text
Pipeline.largerThan(
    tensor1: Tensor,
    tensor2: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `tensor1` | 输入 | 左操作数张量。 |
| `tensor2` | 输入 | 右操作数张量（形状需匹配）。 |
| `result` | 结果 | 在 `tensor1 > tensor2` 处为非零值。 |
## 空间模式说明

* 操作数的形状必须兼容。
* 可用于阈值判断（与常量张量比较），再通过 [bytewiseAny](zh-reference-operators-bytewise-any) 归约，作为 [submit](zh-reference-operators-submit) 的门控条件。

## 相关算子

* [largerEqual](zh-reference-operators-larger-equal) — 包含相等情况的变体。
* [smallerThan](zh-reference-operators-smaller-than) / [smallerEqual](zh-reference-operators-smaller-equal) — 相反方向的比较。

