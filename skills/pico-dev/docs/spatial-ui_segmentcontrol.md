SegmentControl 是一种用于在多个互斥选项中进行切换的组件，它通常由一系列并排的图标或者文本选项组成，用户通过点击选择其中一项可修改展示效果。在形态上可分为 SegmentControl 容器与 SegmentItem 容器子项。

## 使用限制
组件的最小高度由 `SegmentControlDefaults.Small.height` 控制，当前为 40 dp。
## API Surface

* SegmentControl
   * `backgroundColor`：SegmentControl 容器背景色，默认由 `PicoTheme.colorTokens.FillTertiaryAlpha` 方法提供。
   * `itemSpace`: 水平方向每个 SegmentItem 之间的距离，默认由 `SegmentControlDefaults.ItemSpace` 方法提供（4 dp）。
   * `contentPadding`：SegmentControl 的内边距，默认由 `SegmentControlDefaults.ContainerPadding` 方法提供（4 dp）。
   * `cornerRadius`：控制 SegmentControl 的 shape 圆角，默认由 `SegmentControlDefaults.Small.containerCornerRadius()` 方法提供。
   * `content`：提供内容，内部包含一个或者多个 SegmentItem。
* SegmentItem
   * `selected`：当前 SegmentItem 是否被选中。
   * `onClick`：用户点击当前 SegmentItem 时触发的回调函数。
   * `textStyle`：提供 SegmentItem 的文本样式，默认由 `SegmentControlDefaults.Small.textStyle()` 方法提供。
   * `colors`：SegmentItem 的颜色值，用于提供当前被选中或者非选中状态下的颜色值，默认由 `SegmentControlDefaults.colors()` 方法提供。
   * `title`：SegmentItem 的自定义展示内容，通常为 `Text`。
   * `icon`：SegmentItem 的自定义展示内容，通常为 `Icon`，如果 `title` 与 `icon` 同时存在，将以垂直方向依次排列 `icon` 与 `title`。
   * `contentPadding`：SegmentItem 的内边距，默认由 `egmentControlDefaults.Small.itemContentPadding()` 方法提供。
   * `gap`：控制 `icon` 与 `title` 之间的边距，默认由 `SegmentControlDefaults.ItemGap` 方法提供。
   * paddings：MenuItem 的内边距 。
   * cornerSize：圆角尺寸。

## 基础用法
```Kotlin
var selectIndex by remember { mutableStateOf(0) }
SegmentControl {
    // 设定5个SegmentItem
    repeat(5) { index ->
        SegmentItem(
            icon = {
                AnyIcon(
                    iconSize = 16.dp,
                )
            },
            selected = selectIndex == index,
            onClick = { selectIndex = index }
        )
    }
}
```


## **高阶用法**
可以通过 `backgroundColor`，`cornerRadius` 等属性修改 SegmentControl 布局背景样式，也可以通过 `SegmentControlDefaults.colors` 的方式自定义 `colors`，实现更多选中与非选中的 SegmentItem 效果。
```Kotlin
@Composable
fun SegmentControlDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.width(400.dp)) {
        var selectIndex by remember { mutableStateOf(0) }
        // 修改默认颜色为黑色,圆角为10dp
        SegmentControl(backgroundColor = Color.Black, contentPadding = 6.dp, cornerRadius = 10.dp) {
            repeat(5) { index ->
                // 同时展示icon 与 title，并且设置两者之间距离为gap 6dp
                SegmentItem(
                    icon = {
                        AnyIcon(
                            iconSize = 16.dp,
                        )
                    },
                    title = {
                        Text(index.toString())
                    },

                    // 自定义选中的颜色，默认 SegmentItem为白色White，内容为LightGray，选中时为Red，White
                    colors = SegmentControlDefaults.colors(Color.White,Color.LightGray,Color.Red,Color.White),
                    gap = 6.dp,
                    selected = selectIndex == index,
                    onClick = { selectIndex = index }
                )
            }
        }
    }
}
```


