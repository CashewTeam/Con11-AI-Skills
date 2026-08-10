将张量归约为单一条件，只要**任一**字节/元素非零该条件即为真。可与比较算子搭配，根据“至少一个元素通过”来控制计算图的行为。
## 签名
```text
Pipeline.bytewiseAny(
    operand: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类别 | 说明 |
| --- | --- | --- |
| `operand` | 输入 | 掩码张量（通常来自比较算子）。 |
| `result` | 结果 | 只要 `operand` 中有任一元素非零即为非零。 |
## 空间模式说明

* 典型用法：`largerThan` → `bytewiseAny` → 将结果作为 [submit](zh-reference-operators-submit) 的 `condition` 参数，使某个阶段在至少一个元素通过时执行。
* 如需“所有元素都通过”的测试，请使用 [bytewiseAll](zh-reference-operators-bytewise-all)。

## 相关算子

* [bytewiseAll](zh-reference-operators-bytewise-all) —— 只有全部元素非零时才为真。
* 比较算子：[equal](zh-reference-operators-equal)、[largerThan](zh-reference-operators-larger-than) 等。
* [submit](zh-reference-operators-submit) —— 条件执行。

