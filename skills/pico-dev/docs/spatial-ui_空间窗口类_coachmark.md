Coachmark 是在 PICO 设计规范下，以锚点为基础进行内容展示的组件。Coachmark 分为锚点与内容，CoachmarkBox 提供基础的展示锚点，配合 SimpleCoachmark、RichCoachmark 以及 ImageCoachmark 等完成最终的内容展示。

* CoachmarkBox：它是所有 Coachmark 的容器，用于提供子内容 Coachmark 的锚点。
* SimpleCoachmark：用于展示简单信息，如文本、可选的按钮的 Coachmark。
* RichCoachmark：用于展示多种信息，包含图片、标题、内容、按钮的 Coachmark。
* ImageCoachmark：用于展示图片信息与可选按钮的 Coachmark。

## API Surface

* CoachmarkBox
   * `coachmark`：用于展示内容的 Coachmark，子内容通常是 SimpleCoachmark、RichCoachmark、ImageCoachmark。
   * `showCoachmark`：是否显示 Coachmark，布尔值，默认值为 true。
   * `direction`：Coachmark 相对于 CoachmarkBox 锚点视图的方向。默认值的方向（CoachmarkDirection）的 ToEnd，即展示在 CoachmarkBox 的右侧。
   * `gap`：CoachmarkBox 与 Coachmark 之间的间距，默认由 `CoachmarkDefaults.DefaultGap` 提供。
   * `content`：当前 CoachmarkBox 展示的内容。
* SimpleCoachmark
   * `text` ：当前 SimpleCoachmark 的内容，通常为 `Text`，也可以是自定义的其他内容。
   * `button` ：SimpleCoachmark 中可选按钮内容，可以传入自定义内容
   * `backgroundColor` ：用于设置 SimpleCoachmark 的背景色，默认由 `CoachmarkDefaults.DefaultBackgroundColor` 方法提供。
   * `cornerSize` ：用于设置 SimpleCoachmark 的背景圆角半径。
* RichCoachmark
   * `image`：当前 RichCoachmark 的图片。
   * `title` ：当前 RichCoachmark 的标题。
   * `buttons `：RichCoachmark 中可选按钮内容，可以传入自定义内容。
   * `backgroundColor` ：用于设置 RichCoachmark 的背景色，默认由 `CoachmarkDefaults.DefaultBackgroundColor` 方法提供。
   * `cornerSize` ：用于设置 RichCoachmark 的背景圆角半径。
   * `content`：用于设置 RichCoachmark 的主要内容。
* ImageCoachmark
   * `image`：当前 ImageCoachmark 的内容，通常为 `Image`。
   * `button`：ImageCoachmark 中可选按钮内容，可以传入自定义内容。
   * `backgroundColor`：用于设置 ImageCoachmark 的背景色，默认由 `CoachmarkDefaults.DefaultBackgroundColor` 方法提供。
   * `cornerSize` ：用于设置 SimpleCoachmark 的背景圆角半径。
   * `padding`：ImageCoachmark 的内边距，默认为 8 dp。

## 基础用法
```Kotlin
@Composable
fun CurrentCoachmarkDemo() {
    // 控制当前CoachmarkBox中的coachmark是否展示
    var showCoachmark by remember { mutableStateOf(false) }
    CoachmarkBox(showCoachmark = showCoachmark, coachmark = {
        // 展示SimpleCoachmark
        SimpleCoachmark(
            text = { Text("Hello World") },
            button = {
                CoachmarkDefaults.CoachmarkButton(
                    onClick = { showCoachmark = false }
                ) {
                    Text("Action")
                }
            }
        )
    }) {
        IconButton(
            onClick = { showCoachmark = !showCoachmark },
            size = IconButtonDefaults.iconButtonSize(40.dp)
        ) {
            Icon(
                painter = painterResource(R.drawable.ic_sample_circle_placeholder),
                null
            )
        }
    }
}
```


## **高阶用法**

* 可修改 CoachmarkBox direction，从而达到不同的锚点方向展示。
* 可搭配 RichCoachmark 、 ImageCoachmark 实现更多 Coachmark 展示效果。

```Kotlin
@Composable
fun CurrentCoachmarkDemo() {
    // 控制当前CoachmarkBox中的coachmark是否展示
    var showCoachmark by remember { mutableStateOf(false) }
    // 设置coachmark展示在左边
    CoachmarkBox(direction = CoachmarkDirection.ToStart , showCoachmark = showCoachmark, coachmark = {
        // 展示RichCoachmark，配置image、title、buttons、content等内容
        RichCoachmark(
            image =
                {
                    Image(
                        painter =
                            painterResource(
                                R.drawable.img_sample_header_of_modal_sheet
                            ),
                        contentDescription = null,
                        contentScale = ContentScale.Crop
                    )
                },
            title = { Text("Rich Coachmark Title") },
            content = {
                Text("Provide tips that will be useful to the reader navigating your app")
            },
            buttons = {
                CoachmarkDefaults.CoachmarkButton(
                    onClick = { showCoachmark = false }
                ) {
                    Text("Action")
                }
                CoachmarkDefaults.CoachmarkButton(
                    onClick = { showCoachmark = false }
                ) {
                    Text("Action")
                }
            }

        )
    }) {
        IconButton(
            onClick = { showCoachmark = !showCoachmark },
            size = IconButtonDefaults.iconButtonSize(40.dp)
        ) {
            Icon(
                painter = painterResource(R.drawable.ic_sample_circle_placeholder),
                null
            )
        }
    }
```


```Kotlin
@Composable
fun CurrentCoachmarkDemo() {
    // 控制当前CoachmarkBox中的coachmark是否展示
    var showCoachmark by remember { mutableStateOf(false) }
    // 设置coachmark展示在下面
    CoachmarkBox(direction = CoachmarkDirection.Below , showCoachmark = showCoachmark, coachmark = {
        // ImageCoachmark，配置image
        ImageCoachmark(
            image = {
                Image(
                    painter =
                        painterResource(
                            R.drawable.img_sample_header_of_modal_sheet
                        ),
                    contentDescription = null,
                    contentScale = ContentScale.Crop
                )
            },
        )
    }) {
        IconButton(
            onClick = { showCoachmark = !showCoachmark },
            size = IconButtonDefaults.iconButtonSize(40.dp)
        ) {
            Icon(
                painter = painterResource(R.drawable.ic_sample_circle_placeholder),
                null
            )
        }
    }
}
```


