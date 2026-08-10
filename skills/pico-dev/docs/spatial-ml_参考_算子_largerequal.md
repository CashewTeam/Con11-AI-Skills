逐元素执行大于等于比较（`tensor1 >= tensor2`），将布尔风格的结果写入结果张量。
## 签名
```text
Pipeline.largerEqual(
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
| `result` | 结果 | 在 `tensor1 >= tensor2` 处为非零值。 |
## 空间模式说明

* 操作数的形状必须兼容。
* 可使用 [bytewiseAll](zh-reference-operators-bytewise-all) / [bytewiseAny](zh-reference-operators-bytewise-any) 将结果归约为单一条件值。

## 相关算子

* [largerThan](zh-reference-operators-larger-than) — 严格大于的变体。
* [smallerThan](zh-reference-operators-smaller-than) / [smallerEqual](zh-reference-operators-smaller-equal) — 相反方向的比较。

