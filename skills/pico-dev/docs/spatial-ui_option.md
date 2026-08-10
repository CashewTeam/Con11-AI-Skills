Option 是 PICO 设计规范下的一种具有“选中”状态的基础组件。您可以组合多个 Option，自由实现“多选”、“单选”场景。

## API Surface

* `selected`：标记此项是否被选中。
* `onSelectChange`：当选中状态变化时，会触发此回调。例如用户点击了 Option。
* `content`：Option 的内容区域，通常搭配 `Text` 使用。默认情况下颜色跟随 `colors` 参数定义。
* `icon`：可选，为 Option 的图标，通常搭配 `Icon` 使用。默认情况下图标跟随 `colors` 中的 `contentColor`，如果您想保留 `Icon` 图标原始颜色，可以将 `Icon` 的 `tint` 参数设置为 `Color.Unspecified`。
* `enabled`：设置此控件是否生效。

## 基础用法
```Kotlin
@Composable
fun OptionSimpleSample() {
    var checked by remember { mutableStateOf(false) }
    Option(
        selected = checked,
        onSelectChange = { checked = !checked }
    ) {
        Text("label")
    }
}
```


以上代码会创建一个最初处于未选中状态的 Option。当用户点击 Option 时，`onSelectChange lambda` 会更新 `checked` 状态。下面是一个带有 `Icon` 的 Option 例子：
```Kotlin
@Composable
fun OptionWithIconSample() {
    var checked by remember { mutableStateOf(false) }
    Option(
        selected = checked,
        onSelectChange = { checked = !checked },
        icon = {
            Icon(
                painter = painterResource(R.drawable.Start),
                contentDescription = null
            )
        }
    ) {
        Text("Star")
    }
}
```


## **高阶用法**
### 自定义颜色
通过设置 `colors` 参数，结合`OptionDefaults.optionColors()`函数，开发者可以自定义 Option 的颜色。如下：
```Kotlin
@Composable
private fun 
OptionSample() {
    var selected by remember { mutableStateOf(false) }
    Option(
        selected = selected,
        onSelectChange = { selected = it },
        icon = {
            Icon(
                painter = painterResource(R.drawable.ic_sui_rating_star),
                contentDescription = null
            )
        },
        colors = OptionDefaults.optionColors(
            checkedContentColor = Color.Red,
            checkedContainerColor = Color.Yellow,
            unCheckedContentColor = Color.Blue,
            unCheckedContainerColor = Color.Gray
        )
    ) {
        Text("Star")
    }
}
```


### 多选&单选
Option 可以搭配其他容器，如 Column、Row、FlowRow 使用。您可以组合多个 Option，自定义单选或者多选操作。
如下例子，有一组数据定义：
```Kotlin
class Item(val title: String) {
    // selected 定义为State，当它变化时，可以触发Compose重组
    var selected by mutableStateOf(false)
}
// 定义了一组选项
val items = listOf(
    Item("Option 1"),
    Item("Option 2"),
    Item("Option 3"),
    Item("Option 4"),
    Item("Option 5"),
)
```

#### 多选
期望用户可以选择多种选项时，可以编辑如下代码：
```Kotlin
@Composable
private fun OptionMultiSelectionSample() {
    val selectedInfo = items.filter { it.selected }.joinToString(separator = "、") { it.title }
    Column {
        // 展示选择的结果
        Text("You've selected：$selectedInfo")
        // 可以使用流式布局来承载标签
        FlowRow(modifier = Modifier.border(1.dp, Color.Gray)) {
            items.forEach { item ->
                Option(
                    // 3 Option的状态
                    selected = item.selected,
                    // 4 点击后更改选中状态
                    onSelectChange = { item.selected = it },
                    modifier = Modifier.padding(4.dp)
                ) {
                    Text(item.title)
                }
            }
        }
    }
}
```


#### 单选
需要约束用户只允许选择一个选项时：
```Kotlin
@Composable
private fun OptionSingleSelectionSample() {
    val selectedInfo = items.filter { it.selected }.joinToString(separator = "、") { it.title }
    Column {
        // 展示选择的结果
        Text("You've selected：$selectedInfo")
        // 可以使用流式布局来承载标签
        FlowRow(modifier = Modifier.border(1.dp, Color.Gray)) {
            items.forEach { item ->
                Option(
                    selected = item.selected,
                    onSelectChange = {
                        // 重置其他Item的选中状态
                        items.forEach { it.selected = false }
                        // 更新当前Option的选中状态
                        item.selected = it
                    },
                    modifier = Modifier.padding(4.dp)
                ) {
                    Text(item.title)
                }
            }
        }
    }
}
```


