SearchField 是在 PICO 设计规范下，允许用户输入文本，并通过按下键盘上的搜索按钮或其他方式触发搜索操作的组件。

## API Surface

* `value`：SearchField 中的当前文本值。
* `onValueChange`：当 SearchField 中的文本发生变化时调用的回调函数。它将新的文本值作为参数。
* `onSearch`：当用户点击软件键盘上的搜索按钮时触发的回调。
* `placeholder`：在搜索框为空时显示的占位符内容，一般为文本。
* `leadingContent`：用于在搜索框开头显示自定义内容。默认为 `SearchFieldDefaults.searchIcon` 提供的搜索图标。
* `enabled`：布尔值，是否搜索框启用。设置为 false 时，搜索框既不可编辑也不可聚焦。
* `textStyle`：应用于搜索框中输入文本的文本样式。默认为 `SearchFieldDefaults.DefaultTextStyle` 中定义的样式。
* `interactionSource`：表示此 SearchField 交互流的 `MutableInteractionSource`。可传入自定义 `MutableInteractionSource` 观察 SearchField 的交互行为。
* `cornerRadius`：搜索框的圆角半径。默认为 100.dp。
* colors：设置搜索框的颜色值，包括背景颜色、文字颜色、placeholder 颜色等，默认由 `SearchFieldDefaults.searchFieldColors` 中定义的颜色提供。

## 基础用法
```Java
@Composable
fun SimpleSearchFieldSample() {
    var value by remember { mutableStateOf("") }
    var searchValue by remember { mutableStateOf("") }
    Column {
        SearchField(
            value = value,
            onValueChange = { value = it },
            onSearch = {
                searchValue = value
            },
        )
        Text("searchFor: $searchValue")
    }
}
```


## **高阶用法**
可以通过自定义 SearchField 中的 `placeholder` 与 `leadingContent`，实现自定义图标修改。
```Java
@Composable
fun SimpleSearchFieldSample() {
    var value by remember { mutableStateOf("") }
    var searchValue by remember { mutableStateOf("") }
    Column {
        SearchField(
            value = value,
            onValueChange = { value = it },
            placeholder = { Text(text = "Search") },
            onSearch = {
                searchValue = value
            },
            leadingContent = { Icon(painter = painterResource(R.drawable.ic_sample_voice), null)
            },
            colors = SearchFieldDefaults.searchFieldColors(textColor = Color.Red, backgroundColor = Color.Black, focusedColor = Color.Black, placeholderColor = Color.White)
        )
        Text("searchFor: $searchValue")
    }
}
```


