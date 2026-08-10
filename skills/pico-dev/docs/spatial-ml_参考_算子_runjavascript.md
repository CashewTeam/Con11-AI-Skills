将一段 JavaScript 代码作为计算图的一个阶段来运行，张量通过中缀 I/O 辅助函数绑定为输入和输出。当某段图逻辑用脚本表达比用一串数学/比较算子更清晰时，可以使用它。
## 签名
```text
Pipeline.runJavaScript(
    script: String,
    // tensors wired in/out via infix helpers:
    //   tensor into "name"          -> input only
    //   tensor outFrom "name"       -> output only
    //   tensor intoAndOutFrom "name"-> input and output
)
```

`into`、`outFrom` 和 `intoAndOutFrom` 这几个中缀辅助函数为张量命名，使脚本可以通过这些名称读写它们。
## 参数 / 结果
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `script` | 输入 | 为该阶段执行的 JavaScript 源代码。 |
| `into` | 输入 | 将张量绑定为一个具名的脚本输入。 |
| `outFrom` | 结果 | 将张量绑定为一个具名的脚本输出。 |
| `intoAndOutFrom` | 输入/输出 | 将张量同时绑定为输入和输出。 |
## 空间模式说明

* 脚本在运行时的沙箱内执行；请把它当作纯粹的“张量输入 / 张量输出”逻辑，而不是通用的应用代码。
* 优先使用专用的数学/比较算子——它们更快也更清晰。仅在控制流或无法整洁映射到单个算子的定制化逐元素逻辑中才使用脚本。

## 相关算子

* [arithmetic](zh-reference-operators-arithmetic) —— 无需脚本的表达式运算。
* 比较算子：[equal](zh-reference-operators-equal)、[largerThan](zh-reference-operators-larger-than) 等。
* [submit](zh-reference-operators-submit) —— 执行计算图。

