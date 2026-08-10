Toolbar 是在 PICO 设计规范下，一种被放置在 WindowContainer 的底部中央位置的容器，可以用于展示额外的提示控件。

## API Surface

* `cornerSize`：控制 Toolbar 的圆角半径。默认值为 16 dp。
* `followViewpoints`：工具栏要跟随的 ViewPoint，默认为 `ViewPoint.All`。
* `content`：Toolbar 内部放置的内容。

## 基础用法
```Kotlin
@Preview
@Composable
private fun ToolbarDemo() {
    Toolbar {
        repeat(4) {
            Box {
                Button(
                    onClick = { // 自定义内容}
                    },
                    colors = IconButtonDefaults.iconButtonColors(containerColor = Color.Transparent)
                ) {
                    Text("Action")
                }
            }
        }
    }
}
```


## **高阶用法**
可通过配置 Toolbar 的 `cornerSize`，从而自定义其内容。
```Kotlin
@Preview
@Composable
private fun ToolbarDemo() {
    Toolbar(cornerSize = 0.dp) {
        repeat(4) {
            Box {
                Button(
                    onClick = { // 自定义内容}
                    },
                    colors = IconButtonDefaults.iconButtonColors(containerColor = Color.Transparent)
                ) {
                    Text("Action")
                }
            }
        }
    }
}
```


