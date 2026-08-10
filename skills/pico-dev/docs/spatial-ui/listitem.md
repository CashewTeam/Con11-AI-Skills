ListItem 是 PICO 设计规范下，用于承载竖直列表中通用的信息展示组件，常作为 Column、LazyColumn 的内容。该组件由一个必要的左侧标题区域以及可选的左侧图标区、右侧内容区和可选标题组成。

## API Surface

* `headlineContent`：标题区域，内容常为`Text`。
* `leadingContent`：左侧区域，可选，内容常为 `Icon` 或者 `Image`。
* `trailingContent`：右侧区域，可选，内容常搭配 `Icon`、`Button`、`Badge` 以及 `Switch` 等组件使用。
* `supportingContent`：副标题区域，可选，通常为 `Text`，可以用于对标题的补充，承载更详细的信息。
* `colors`：组件内置了 PICO 标准色值，可通过此参数自定义颜色。
* `padding`：ListItem 的内容间距，一般无需调整。
* `shape`：ListItem 的背景形状，可通过此参数定义圆角大小等参数。

## 基础用法
ListItem 通常作为 `Column` 或者 `LazyColumn` 的内容来使用。
```Kotlin
@Composable
fun SimpleListItemSample() {
    Column {
        ListItem(headlineContent = { Text(text = "Title 1") })
        // 可以添加更多ListItem
    }
}
```


## 高阶用法
ListItem 的 `leadingContent`、`trailingContent`、`supportingContent` 是可选的，您可以基于这些可选槽位灵活定义不同的样式。
```Kotlin
@Composable
fun Demo() {
    Column {
        ListItem(
            headlineContent = { Text(text = "这是列表区域") },
            leadingContent = {
                // 通常可以是Icon 或者Image，AsyncImage（Coil，支持网络图片）
                // 这个区域通常可以是消息列表的头像、新闻的头图
            },
            trailingContent = {
                // 尾部区域，可以搭配各种控件使用，例如Icon、Button、Badge
                // 例如展示消息未读数、设置页的开关等
            },
            supportingContent = {
                // 通常是Text
            }
        )
    }
}
```

使用示例如下，通常可以开发出右图中的样式：
```Kotlin
@Composable
fun Demo() {
    Column {
        ListItem(
            headlineContent = { Text(text = "List Title") },
            leadingContent = {
                Image(
                    painter = painterResource(R.drawable.image_container),
                    contentDescription = null
                )
            },
            supportingContent = {
                Text(text = "Supporting line text lorem ipsum dolor sit amet, consectetur")
            },
            trailingContent = {
                Icon(
                    painter =painterResource(id =R.drawable.ic_sui_settinglistitem_trail_arrow),contentDescription = null
                )
            }
        )
        // with checkbox
        ListItem(
            headlineContent = { Text(text = "List Title") },
            leadingContent = {
                Icon(painter = painterResource(R.drawable.ic_sample_placeholder),null)
            },
            trailingContent = {
                Box(modifier = Modifier.padding(start = 8.dp, end = 10.dp)) {
                    var checked by remember { mutableStateOf(false) }
                    Switch(checked, onCheckedChange = { checked = it })
                }
            }
        )
    }
}
```


