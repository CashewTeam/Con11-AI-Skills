Button 是 PICO 设计规范下一种常见的控件，通常用来响应用户的点击行为。Spatial UI 组件库中内置了若干种 PICO 品牌风格样式的 Button，您也可以通过改变参数，使按钮符合自己的预期效果。通常需要配合 `Text` 一起使用。

## API Surface

* `onClick`：点击的回调函数。
* `enabled`：设置控件是否可用。
* `size`：控件尺寸，可通过 `ButtonDefaults.buttonSize` 方法进行自定义。取值为 `ButtonDefaults.Regular` 表示使用默认尺寸。
* `colors`：控件颜色，可通过 `ButtonDefaults.buttonColors` 方法进行自定义，可定义 `containerColor` 背景颜色， `contentColor` 内容颜色。
* `leadingIcon`：首部显示图标，可选，通常为 `Icon`。
* `trailingIcon`：尾部显示图标， 可选，通常为 `Icon`。
* `contentPadding`：控件内容的内间距。
* `shape`：控件的形状，可自定义。
* `gap`：内容间距，定义 `content` 、 `leadingIcon` 、`trailingIcon` 之间的间距。
* `content`：控件的内容。

## 基础用法
```Kotlin
@Composable
fun ButtonSample() {
    Button(
        onClick = {
            // do something
        }
    ) {
        Text("Click me")
    }
}
```


## 高阶用法
自定义 Button， 通过 `ButtonDefaults.buttonColors` 可自定义颜色，首部、尾部可选添加图标显示。
```Kotlin
@Composable
fun ButtonListSample() {
    Column(
        verticalArrangement = Arrangement.Center,
    ) {
        CustomButton(
            title = "Click me",
            onClick = {},
            leadingIcon = {
                AnyIcon()
            }
        )
        Spacer(Modifier.height(10.dp))
        CustomButton(
            title = "Click me",
            onClick = {},
            trailingIcon = {
                AnyIcon()
            }
        )
        Spacer(Modifier.height(10.dp))
        CustomButton(
            title = "Click me",
            onClick = {},
            leadingIcon = {
                AnyIcon()
            },
            trailingIcon = {
                AnyIcon()
            }
        )
    }
}

@Composable
fun CustomButton(title:String,
                 onClick: () -> Unit,
                 leadingIcon: (@Composable () -> Unit)? = null,
                 trailingIcon: (@Composable () -> Unit)? = null
                 ) {
    Button(
        onClick = onClick,
        size = ButtonDefaults.Regular,
        colors = ButtonDefaults.buttonColors(
            containerColor = Color(color = 0xFF3D8BFF),
            contentColor = Color(color = 0xFFFFFFFF)
        ),
        enabled = true,
        leadingIcon = { leadingIcon?.invoke() },
        trailingIcon = { trailingIcon?.invoke() }
    ) {
        Text(text = title)
    }
}
```


