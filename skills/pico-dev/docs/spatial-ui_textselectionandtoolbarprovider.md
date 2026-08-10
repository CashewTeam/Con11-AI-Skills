TextSelectionAndToolbarProvider 是在 PICO 设计规范下，提供文本选择与 toolbar 颜色配置的组件，常见于 TextField 的光标、选中颜色更改或者展示 toolbar 等场景。

## API Surface

* `toolbar`：用于在 `content` 展示 toolbar。
* `colors`：用于定制 TextField 等组件的光标颜色以及选中文本颜色。
* `content`：TextSelectionAndToolbarProvider 的内容。

## 基础用法
```Kotlin
@Composable
private fun SingleLineCustomizeColors() {
    var text by rememberRandomString()
    Title("Single-line text with designated color")
    // 修改光标颜色为红色，选中背景为蓝色
    TextSelectionAndToolbarProvider(
        colors =
            TextSelectionColors(
                handleColor = Color.Red,
                backgroundColor = Color.Blue,
            ),
    ) {
        TextField(
            text,
            onValueChange = {
                text = it
            },
            modifier =
                Modifier
                    .fillMaxWidth()
                    .padding(16.dp),
            singleLine = true,
        )
    }
}
```


## **高阶用法**
可以通过配置不同层级的 TextSelectionAndToolbarProvider，达到显示不同的选中风格。
```Kotlin
@Composable
private fun SingleLineCustomizeColors() {
    var text by rememberRandomString()
    TextSelectionAndToolbarProvider(
        colors =
            TextSelectionColors(
                handleColor = Color.Red,
                backgroundColor = Color.Blue,
            ),
    ) {
        Row {
            // 展示光标为红色,选中颜色为蓝色
            TextField(
                text,
                onValueChange = {
                    text = it
                },
                modifier =
                    Modifier
                        .padding(16.dp),
                singleLine = true,
            )
            // 展示光标为绿,选中颜色为黑色
            TextSelectionAndToolbarProvider(
                colors =
                    TextSelectionColors(
                        handleColor = Color.Green,
                        backgroundColor = Color.Black,
                    ),
            ){
                TextField(
                    text,
                    onValueChange = {
                        text = it
                    },
                    modifier =
                        Modifier
                            .padding(16.dp),
                    singleLine = true,
                )
            }
        }
    }
}
```


