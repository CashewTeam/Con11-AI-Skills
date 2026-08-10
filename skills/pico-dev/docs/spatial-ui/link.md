Link 是 PICO 设计规范下一种没有背景或边框的用于响应用户点击交互的的控件，内容区域通常为文本 `Text` 或其他可组合项，常用于导航链接、了解或查看详情等场景。

## API Surface

* `onClick`：点击控件时执行的回调函数。
* `enabled`：是否可用，布尔值。
* `size`：控件的尺寸，可通过 `LinkDefaults.buttonSize` 方法进行自定义。取值 `LinkDefaults.Regular` 表示默认尺寸。
* `contentPadding`：控件内容的内间距，默认根据 `size` 决定大小，可自定义。
* `shape`：控件的形状。
* `colors`：控件的颜色，可通过 `LinkDefaults.linkColors` 方法自定义 `containerColor`、`contentColor`。
* `trailingIcon`：`@Composable` 回调函数，控件尾部图标，可选，通常为 `Icon`。
* `content`：控件的内容， 通常为 `Text`。

## 基础用法
```Kotlin
@Composable
fun LinkSample() {
    Link(onClick = {}) { Text("Click to learn the details") }
}
```


## 高阶用法
自定义尺寸、颜色、padding、添加尾部图标及形状。
```Kotlin
@Composable
fun LinkDetailSample() {
    Link(
        onClick = {},
        //自定义大小
        size = LinkDefaults.buttonSize(
            height = 24.dp,
            width = 120.dp
        ),
        //自定义颜色
        colors = LinkDefaults.linkColors(
            containerColor = Color.White,
            contentColor = Color.Black
        ),
        //自定义间距
        contentPadding = PaddingValues(horizontal = 15.dp, vertical = 2.dp),
        //自定义尾部图标
        trailingIcon = { AnyIcon(iconSize = 16.dp) })
    {
        Text("Click to View")
    }
}
```


