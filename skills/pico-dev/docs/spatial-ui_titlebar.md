TitleBar 是 PICO 设计规范下，对一行内左、中、右三部分用户自定义样式进行布局的标题栏控件，提供了标题内容绝对居中和相对居中两种模式。

* **绝对居中**

* **相对居中**

## API Surface

* `title`： 标题槽位，可自定义内容。
* `leadingActions`：顶部内容槽位，自定义顶部显示内容，可选项。
* `trailingActions`：尾部内容槽位，自定义尾部显示内容，可选项。
* `leadingGap`：顶部预留空间， 默认 8 dp， 可自定义大小。
* `trailingGap`：尾部预留空间， 默认 8 dp， 可自定义大小。
* `titleAlignment`：title 对齐方式，提供绝对居中和相对居中两种方式，默认相对居中。
* `colors`：titleBar 的颜色设置， 可通过`TitleBarDefaults` 设置 `title` 、`leadingActions` 和 `trailingActions` 的颜色。

## 基础用法
常用于导航栏的显示，添加首部、尾部事件 Items。
```Kotlin
@Composable
fun TitleBarWithCenterTitleSample() {
    TitleBar(
        title = { Text("Title")},
        leadingActions = {
           IconButton (onClick = {}) {
               Icon(
                   painter = painterResource(id = R.drawable.ic_sample_search),
                   contentDescription = null
               )
           }
        },
        trailingActions = {
            IconButton(onClick = {}) {
              Icon(
                  painter = painterResource(id = R.drawable.sample_more),
                  contentDescription = null
              )
           }
        }
    )
}
```


## 高阶用法
自定义标题的对齐方式，可放置多个 Item 在标题槽位，滑动显示，常见于分页控制栏显示。

* **标题的对齐方式**
   * 绝对居中，标题位于导航栏的中间位置。
      ```Kotlin
      @Composable
      fun TitleBarWithCenterTitleSample() {
          Box {
              TitleBar(
                  modifier = Modifier.background(PicoTheme.colorScheme.onAccent),
                  title = { Text("Title") },
                  leadingActions = { SimpleButton() },
                  trailingActions = {
                      SimpleButton()
                      SimpleButton()
                      SimpleButton()
                  },
                  titleAlignment = TitleAlignment.CenterInBar
              )
          }
      }
      ```

   * 相对居中， 标题位于首、尾部中间。
      ```Kotlin
      @Composable
      fun TitleBarStartTitleSample() {
          Box {
              TitleBar(
                  modifier = Modifier.background(PicoTheme.colorScheme.onAccent),
                  title = { Text("Title") },
                  leadingActions = { SimpleButton() },
                  trailingActions = {
                      SimpleButton()
                      SimpleButton()
                      SimpleButton()
                  },
                  titleAlignment = TitleAlignment.Center
              )
          }
      }
      ```

* **在分页导航栏场景中的使用**
   * 添加多个分页对应的 Item，滑动显示。
      ```Kotlin
      @Composable
      fun TitleBarMultipleTitlesAndActionsSample() {
          TitleBar(
              modifier = Modifier.background(PicoTheme.colorScheme.onAccent),
              titleAlignment = TitleAlignment.Center,
              title = {
                  val scrollState = rememberScrollState()
                  Row(
                      modifier = Modifier
                          .horizontalScroll(scrollState)
                          .padding(horizontal = 24.dp),
                      horizontalArrangement = Arrangement.spacedBy(8.dp)
                  ) {
                      Item(text = "Item")
                      Item(text = "Item")
                      Item(text = "Item")
                      Item(text = "Item")
                      Item(text = "Item")
                      Item(text = "Item")
                      Item(text = "Item")
                  }
              },
              leadingActions = {
                  SimpleButton()
                  SimpleButton()
              },
              trailingActions = {
                  SimpleButton()
                  SimpleButton()
                  SimpleButton()
                  SimpleButton()
              }
          )
      }
      ```

   * 添加侧边遮罩渐变优化多个 Item 时的滑出效果。
      ```Kotlin
      @Composable
      fun TitleBarMultipleTitlesAndActionsSample2() {
          TitleBar(
              modifier = Modifier.background(PicoTheme.colorScheme.onAccent),
              titleAlignment = TitleAlignment.Center,
              title = {
                  val scrollState = rememberScrollState()
                  Row(
                      modifier =
                      Modifier
                          .graphicsLayer(compositingStrategy = CompositingStrategy.Offscreen)
                          .drawWithContent {
                              drawContent()
                              //绘制渐变半透遮罩
                              drawRect(
                                  brush =
                                  Brush.linearGradient(
                                      listOf(Color.Black, Color.Transparent),
                                      end = Offset(size.width, 0f)
                                  ),
                                  topLeft = Offset(size.width - 30.dp.toPx(), 0f),
                                  size = Size(width = 30.dp.toPx(), height = size.height),
                                  blendMode = BlendMode.DstIn,
                              )
                          }
                          .horizontalScroll(scrollState)
                          .padding(horizontal = 24.dp),
                      horizontalArrangement = Arrangement.spacedBy(8.dp)
                  ) {
                      Item(text = "Item")
                      Item(text = "Item")
                      Item(text = "Item")
                      Item(text = "Item")
                      Item(text = "Item")
                      Item(text = "Item")
                      Item(text = "Item")
                  }
              },
              leadingActions = {
                  SimpleButton()
                  SimpleButton()
              },
              trailingActions = {
                  SimpleButton()
                  SimpleButton()
                  SimpleButton()
                  SimpleButton()
              }
          )
      }
      ```

