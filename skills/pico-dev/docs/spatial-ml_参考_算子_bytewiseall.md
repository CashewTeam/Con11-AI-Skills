将张量归约为单一条件，只有当**所有**字节/元素都非零时该条件才为真。可与比较算子搭配，将逐元素掩码转换为计算图可用于判断的单个布尔值——例如作为 [submit](zh-reference-operators-submit) 的条件。
## 签名
```text
Pipeline.bytewiseAll(
    operand: Tensor,
    result: Tensor,
)
```

## 参数 / 结果
| 名称 | 类别 | 说明 |
| --- | --- | --- |
| `operand` | 输入 | 掩码张量（通常来自比较算子）。 |
| `result` | 结果 | 仅当 `operand` 的每个元素都非零时才为非零。 |
## 空间模式说明

* 典型用法：`largerThan` → `bytewiseAll` → 将结果作为 [submit](zh-reference-operators-submit) 的 `condition` 参数，使某个阶段仅在整个区域都通过测试时才执行。
* 如需“任一元素通过即可”的测试，请使用 [bytewiseAny](zh-reference-operators-bytewise-any)。

## 相关算子

* [bytewiseAny](zh-reference-operators-bytewise-any) —— 只要有任一元素非零即为真。
* 比较算子：[equal](zh-reference-operators-equal)、[largerThan](zh-reference-operators-larger-than) 等。
* [submit](zh-reference-operators-submit) —— 条件执行。

