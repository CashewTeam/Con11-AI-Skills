Sheet 是在 PICO 设计规范下，用于呈现弹出内容的组件，可以承担弹窗相关的任务。

## API Surface

* `onDismissRequest`：当用户点击弹出框外部时执行回调。
* `properties`：用于设置 Sheet 的行为属性，比如是否可以点击外部，默认由 `SheetDefaults.DefaultSheetsProperties`  方法提供。
* `title`：作为标题显示的组件，通常为文本（`Text`），可以自定义内容。
* `leadingAction`：显示在表单（`Sheet`）顶部左上角的组件，默认为 `DefaultCloseIconButton` 提供的关闭按钮。
* `trailingAction`：显示在表单（`Sheet`）顶部右上角的组件。
* `bottom`：显示在基本表单（`BasicSheet`）底部的组件。
* `content`：`Sheet` 的内容。

## 基础用法
```Kotlin
@Composable
fun SheetDemo() {
    var showSheet by remember { mutableStateOf(false) }

    Button({
        showSheet = !showSheet
    }) {
        Text("Show/Hide Sheet")
    }

    if (showSheet){
        Sheet(
            // 点击了Sheet外部，可以在这里关闭Sheet展示
            onDismissRequest = { showSheet = false},
            // 默认存在关闭按钮，可以设置为null
            leadingAction = null,
        ) {
            Box(modifier = Modifier.size(300.dp)) {
                Image(
                    modifier = Modifier.matchParentSize(),
                    painter = painterResource(id = R.drawable.image_container),
                    contentDescription = "",
                )
            }
        }
    }

}
```


## **高阶用法**

* `content` 可以传入自定义的内容，从而实现自定义的效果。
* `Sheet` 可以添加 `title` 设置标题，通过设置 `leadingAction`、`trailingAction` 或者 `bottom` 可以在 `content` 周围添加内容

```Kotlin
@Composable
fun SheetDemo() {
    var showSheet by remember { mutableStateOf(false) }

    Button({
        showSheet = !showSheet
    }) {
        Text("Show/Hide Sheet")
    }

    if (showSheet){
        Sheet(
            // 点击了Sheet外部，可以在这里关闭Sheet展示
            onDismissRequest = { showSheet = false},
            title = {
                Text("Title")
            },
            leadingAction = {
                Button({
                    showSheet = false
                }) {
                    Text("Left Button")
                }
            },
            trailingAction = {
                Button({
                    showSheet = false
                }) {
                    Text("Right Button")
                }
            },
            bottom = {
                Button({
                    showSheet = false
                }) {
                    Text("Bottom Button")
                }
            }
        ) {
            Box(modifier = Modifier.fillMaxSize()) {
                Image(
                    modifier = Modifier.matchParentSize(),
                    painter = painterResource(id = R.drawable.image_container),
                    contentDescription = "",
                )
            }
        }
    }

}
```


