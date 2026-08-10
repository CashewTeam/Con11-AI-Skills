在应用启动时，默认的空间容器会首先被打开，展示应用的首个界面。另外，你也可以使用 PICO Spatial SDK 打开或关闭空间容器。
## 打开 WindowContainer
你可以通过以下两种方式打开 WindowContainer：

* 使用 `Context`：
   ```Kotlin
   val context = LocalContext.current // 创建 context（或者使用其它方式获取你想要的 context）
   context.openWindowContainer(id: String, tag: String? = null, bundle: Bundle? = null)
   ```

* 使用 `SpatialNavigator`（PICO Spatial SDK 提供的专门用于打开和关闭空间容器的类）：
   ```Kotlin
   val spatialNavigator = LocalSpatialNavigator.current // 创建 SpatialNavigator
   spatialNavigator.openWindowContainer(id: String, tag: String? = null, bundle: Bundle? = null)
   ```


若你之后需要精确地关闭某个 WindowContainer，请在调用 `openWindowContainer` 时指定 `tag` 参数。

参数说明如下：
| **参数** | **是否必填** | **描述** |
| --- | --- | --- |
| id | 是 | WindowContainer 的名称。 |
| tag | 否 | 打开 WindowContainer 时附加的自定义标签。 ;; * 调用 `openWindowContainer` 时，如果 `id` 相同且 `tag == null`，为“新建”模式，即每次都会打开一个新的 WindowContainer。 ;  * 调用 `openWindowContainer` 时，如果 `id` 相同且 `tag != null`，为“复用”模式，即第一次创建后，每次调用 `openWindowContainer` 都会将原来的窗口调回前台。 |
| bundle | 否 | 自定义的透传数据，可在 WindowContainer 的内容根节点获取。 |

例如，如果要将 `NewsContent` 的标题作为一种数据，在打开它所在的 WindowContainer 的时候把标题传递给它，可以使用以下步骤：

1. 在声明名为 “NewsWindow” 的 WindowContainer 时，为它的内容根节点获取 bundle。
   ```Kotlin
   WindowContainer(
       id = "NewsWindow",
       form = Form.IN_VOLUME,
       resizeType = ContainerResizeType.ContentMinSize,
       size = ContainerSize(defaultWidth = 1280.dp, defaultHeight = 720.dp),
       enableMaterialBackground = false
   ) {
       NewsContent(this.bundle)
   }
   ```

2. 在打开名为 “NewsWindow” 的 WindowContainer 时，把标题转换为 bundle 传入的参数。
   ```Kotlin
   @Composable 
   fun OpenWindowContainerSample() { 
       val spatialNavigator = LocalSpatialNavigator.current
       val newsTitle = "\uD83D\uDDBC\uFE0F 2D & 3D Content Layout \uD83D\uDDFF"
       PicoTheme {
           Button( 
               onClick = {
                   spatialNavigator.openWindowContainer(
                       "NewsWindow",
                       "news-1",
                       Bundle().apply { putString("TITLE", newsTitle) }) 
               }
           ) {
               Text( 
                   text = "Open News Window", 
                   fontSize = 28.sp, 
                   fontFamily = FontFamily.Serif, 
               ) 
           }
       }
   } 
   ```

3. 在 `NewsContent` 里通过 bundle 获取并使用数据。
   ```Kotlin
   @Composable 
   fun NewsContent(bundle: Bundle? = null) { 
       val newsTitle = bundle?.getString("TITLE") ?: "Fail to pass in data!"
       PicoTheme {
           Column( 
               modifier = Modifier 
                   .fillMaxSize() 
                   .background( 
                       color = PicoTheme.colorScheme.accent.copy(alpha = 0.9f), 
                       shape = RoundedCornerShape(60.dp) 
                   ) 
                   .padding(vertical = 30.dp, horizontal = 30.dp), 
               horizontalAlignment = Alignment.CenterHorizontally, 
               verticalArrangement = Arrangement.spacedBy(30.dp), 
           ) {
               Text( 
                   text = newsTitle, 
                   color = PicoTheme.colorScheme.onAccent, 
                   fontSize = 50.sp, 
                   fontFamily = FontFamily.Serif 
               ) 
               // Other content... 
           } 
       } 
   } 
   ```


## 关闭 WindowContainer
你可以通过 `Context` 或 `SpatialNavigator` 关闭 WindowContainer。
```Kotlin
// 关闭当前 WindowContainer
// 当前的 WindowContainer 仅能通过 SpatialNavigator 来关闭
spatialNavigator.closeWindowContainer()

// 批量关闭同名 WindowContainer
context.closeWindowContainer(id)
// 或
spatialNavigator.closeWindowContainer(id)

// 精准关闭某一个在打开时 tag != null 的 WindowContainer
context.closeWindowContainer(id, tag)
// 或
spatialNavigator.closeWindowContainer(id, tag)
```

代码示例：
```Kotlin
@Composable
fun CloseWindowContainerSample(bundle: Bundle?) {
    val spatialNavigator = LocalSpatialNavigator.current
    Column {
        Button(onClick = {
            // 关闭名为 "myUniqueWindow" 且打开时指定了 tag = "unique" 的 WindowContainer
            spatialNavigator.closeWindowContainer(id = "myUniqueWindow", tag = "unique")
        }) {
            Text("Close WindowContainers with same name")
        }
        Button(onClick = {
            // 关闭所有名为 "myWindow" 的 WindowContainer
            spatialNavigator.closeWindowContainer(id = "myWindow")
        }) {
            Text("Close WindowContainers with same name")
        }
        Button(onClick = {
            // 关闭当前 WindowContainer
            spatialNavigator.closeWindowContainer()
        }) {
            Text("Close current WindowContainer")
        }
    }
}
```


