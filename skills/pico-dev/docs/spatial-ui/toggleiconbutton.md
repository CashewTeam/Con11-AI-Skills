ToggleIconButton 是 PICO 设计规范下，一种带有二级“状态”的用于响应用户点击交互的控件，内容区域通常为 Icon， 或其他可组合项。

## API Surface

* `checked`：是否被选中。
* `onCheckedChange`：触发改变状态的回调。
* `enabled`：是否可用，布尔值。
* `size`：控件的尺寸，可通过 `ToggleIconButtonDefaults` 方法进行自定义。取值 `Min` 表示使用默认尺寸。
* `colors`：控件的颜色， 可通过 `ToggleIconButtonDefaults` 方法自定义 `checkedContainerColor`、`checkedContainerColor`、`checkedContainerColor`、`checkedContainerColor`。
* `shape`：控件的形状， 默认为圆形 `CircleShape`。
* `content`：控件的内容， 通常为 `Icon`。

## 基础用法
```Kotlin
@Composable
fun ToggleIconButtonSample() {
    var isChecked by remember { mutableStateOf(false) }
    ToggleIconButton(
        checked = isChecked,
        onCheckedChange = { isChecked = !isChecked },
    ) {
        AnyIcon()
    }
}
```


## 高阶用法
在多个具有 toggle 状态的场景下使用，例如收藏、点赞等操作，自定义显示样式及颜色，取消和确认状态切换。

```Kotlin
@Composable
fun ToggleIconButtonSample() {
    var isLike by remember { mutableStateOf(false) }
    var isCollected by remember { mutableStateOf(false) }
    Row {
        ToggleIconButton(
            onCheckedChange = {
                isLike = !isLike
            },
            checked = true,
            colors = ToggleIconButtonDefaults.toggleIconButtonColors(
                checkedContentColor = Color.Black
            )
        ) {
            Icon(
                painter = painterResource(id = if (isLike) R.drawable.sample_like else R.drawable.sample_unlike),
                contentDescription = null
            )
        }
        Spacer(Modifier. width(20.dp))
        ToggleIconButton(
            onCheckedChange = {
                isCollected = !isCollected
            },
            checked = true,
            colors = ToggleIconButtonDefaults.toggleIconButtonColors(
                checkedContentColor = Color.Black
            )
        ) {
            Icon(
                painter = painterResource(id = if (isCollected) R.drawable.sample_collected else R.drawable.sample_uncollect),
                contentDescription = null
            )
        }
    }
}
```

