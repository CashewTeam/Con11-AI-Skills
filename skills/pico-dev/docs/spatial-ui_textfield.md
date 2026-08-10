TextField 是在 PICO 设计规范下，常用于文本输入的组件。当需要观察或控制文本输入的详细状态（如光标位置、选择范围、输入法组合文本等）时，可以使用基于 `TextFieldValue` 参数的重载形式。

## API Surface

* `value`：当前 TextField 的内容。
* `onValueChange`：当 TextField 内容区域发生改变时，会以当前 TextField 修改后的内容作为回调触发函数。
* `placeholder`：当 `value` 内容为空时，会展示 `placeholder` 下展示的内容。
* `leadingContent`：展示在 TextField 最左侧的内容，默认为 null。
* `trailingContent `：展示在 TextField 最右侧的内容，默认为 null。
* `supportingText`：可选的辅助文本，显示在文本字段容器下方。
* `enabled`：控制此文本字段的启用状态。为 false 时，该组件将不响应用户输入，并且在视觉上以及对无障碍服务而言都显示为禁用状态。
* `readOnly`：控制文本字段的可编辑状态。为 true 时，文本字段无法修改。不过，用户可以聚焦并从中复制文本。只读文本字段通常用于显示用户无法编辑的预填充表单。
* `textStyle`：要应用于输入文本的样式。默认文本样式使用主题定义的 LocalTextStyle。
* `isError`：一个控制文本字段错误状态的布尔值。为 true 时，文本字段将以错误颜色突出显示。
* `visualTransformation`：应用于输入文本的转换。默认为 `VisualTransformation.None`。可以通过自定义 `visualTransformation` 达到输入转换的场景，如密码框。
* `keyboardOptions`：应用于输入文本的键盘选项。默认的键盘选项是 `KeyboardOptions.Default`。
* `keyboardActions`：应用于输入文本的键盘操作。默认的键盘操作是 `KeyboardActions.Default`。
* `singleLine`：一个控制文本字段是单行还是多行的布尔值。为 true 时，文本字段为单行；为 false 时，文本字段为多行。
* `maxLines`：文本字段中要显示的最大行数。默认的 maxLines 为 `Int.MAX_VALUE`。
* `minLines`：文本字段中要显示的最小行数。默认的 minLines 为 `1`。
* `interactionSource`：表示此 TextField 交互流的 `MutableInteractionSource`。可传入自定义 `MutableInteractionSource` 观察 TextField 的交互行为。
* `cornerRadius`：TextField 的背景圆角半径。
* `colors`：用于解析在不同状态下文本、内容（包括标签、占位符、前置和后置图标、指示线）以及背景的颜色，默认为 `TextFieldDefaults.textFieldColors`，也可以通过 `TextFieldDefaults.textFieldColors` 函数自定义颜色。

## 基础用法
```Kotlin
@Composable
private fun SimpleTextFieldSample() {
    Column {
        Text("Simple Example")
        var text by remember { mutableStateOf("") }
        TextField(
            value = text,
            onValueChange = { newValue -> text = newValue },
            placeholder = { Text(text = "Placeholder") },
        )
    }
}
```


## **高阶用法**

* 可通过 `placeholder` 设置文本提示。
* 可通过 `isError` 展示错误样式，`isError` 为 `true` 时，展示的颜色取自`colors`中的 `errorColor`，默认由 `TextFieldDefaults.textFieldColors` 提供。
* 搭配 `leadingContent`、`trailingContent` 和 `supportingText` 可以展示更多自定义内容。

```Kotlin
@Composable
private fun TextFieldFullSample() {
    Column {
        Text("Complex Demo")
        var text by remember { mutableStateOf("") }
        var error by remember { mutableStateOf(false) }
        TextField(
            value = text,
            // 例子中，输入9需要展示错误提示
            onValueChange = { newValue ->
                text = newValue
                error = text.contains("9")
            },
            // 默认空白展示
            placeholder = { Text(text = "press 9 to show error") },
            leadingContent = {
                Icon(
                    painter = painterResource(id = R.drawable.ic_sample_search),
                    contentDescription = null,
                    tint = Color(color = 0x4D000000)
                )
            },
            trailingContent = {
                Icon(
                    painter =
                        painterResource(
                            id = com.pico.spatial.ui.design.R.drawable.ic_sui_dropdown_trigger_down
                        ),
                    contentDescription = null,
                    tint = Color(color = 0x4D000000)
                )
            },
            isError = error,
            // 展示supportingText
            supportingText = {
                Text(text = "supporting text supporting text supporting text supporting text")
            }
        )
    }
}
```


