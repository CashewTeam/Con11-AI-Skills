IconButton 是 PICO 设计规范下一种常见的用于响应用户点击交互的控件，和 Button 不同的是，IconButton 的内容区域通常使用 `Icon` 填充（也支持填充 `Text`），而 Button 的内容区域通常为 `Text`。

## API Surface

* `onClick`：点击的回调函数。
* `enabled`：设置控件是否可用。
* `size`：控件尺寸，可通过 `ButtonDefaults.buttonSize` 方法进行自定义。取值为 `IconButtonDefaults.Regular` 表示使用默认尺寸。
* `colors`：控件颜色，可通过 `ButtonDefaults.buttonColors` 方法进行自定义，可定义 `containerColor` 背景颜色， `contentColor` 内容颜色。
* `shape`：控件形状，可自定义。取值为 `CircleShape` 表示使用默认形状。
* `content`：控件内容，通常为 `Icon`。

## 基础用法
默认 IconButton 为圆形，显示主题色。
```Kotlin
/** A simple usage of [IconButton] */
@Composable
fun IconButtonSample() {
    IconButton(
        onClick = {},
    ) {
        AnyIcon(iconSize = 20.dp)
    }
}
```


## 高阶用法
自定义修改 IconButton 的大小、颜色、形状、图标。
```Kotlin
@Composable
fun IconButtonSample() {
    var clickCount by remember { mutableStateOf(0) }
    Column {
        IconButton(
            onClick = {
                clickCount++
            },
            //自定义尺寸
            size = IconButtonDefaults.iconButtonSize(60.dp),
            //自定义颜色
            colors = IconButtonDefaults.iconButtonColors(
                containerColor = Color(color = 0xFFFF4D4D),
                contentColor = Color.White
            ),
            //自定义形状
            shape = RoundedCornerShape(20.dp),
            enabled = true,
        ) {
            //自定义图标
            AnyIcon(iconSize = 20.dp)
        }
        Text(text = "Click count: $clickCount")
    }
}
```


部分使用场景下 IconButton 图标的颜色各不相同，在不改变 IconButton 中 **** `colors` **** 的情况下，为避免受 IconButton 默认颜色的影响，目前有以下两种实现方式。
**方式一**
```Kotlin
IconButton(
    onClick = {

    }
) {
    Image(
        modifier = Modifier.size(20.dp),
        painter = painterResource(id = R.drawable.ic_sample_download),
        contentDescription = null
    )
}
```

**方式二**
```Kotlin
IconButton(
    onClick = {

    }
) {
    Icon(
        painter = painterResource(id = R.drawable.ic_sample_download),
        contentDescription = null,
        tint = Color.Red
    )
}
```

