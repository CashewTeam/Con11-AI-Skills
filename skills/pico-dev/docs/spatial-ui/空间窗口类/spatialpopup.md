你可以使用 SpatialPopup 组件来为应用添加具有空间浮起效果的弹窗（即空间弹窗），并自定义弹窗内的内容和布局。

## API Surface
SpatialPopup 组件的可配置参数如下：
| **参数** | **类型** | **描述** |
| --- | --- | --- |
| onDismissRequest | () -> Unit | 关键回调，在用户点击弹窗外部或按下系统返回键时触发。你必须在此回调中更新状态来关闭弹窗，否则弹窗可能无法被正常关闭。 |
| modifier | Modifier | 应用于弹窗容器的修饰符。可用于设置背景、边框、阴影（如 `Modifier.shadow`）或约束最大尺寸等。 |
| popupPositionProvider | PopupPositionProvider | 高级定位，用于提供弹窗的屏幕坐标。使用 `rememberSpatialPopupPositionProvider()` 可实现弹窗相对于某个锚点（如一个按钮）的精准定位，是实现下拉菜单、提示框（Tooltip）的基础。 |
| cornerRadius | CornerRadius | 弹窗的圆角。直接传入 `Dp` 值（如 `8.dp`）会为四个角统一设置。默认值为 `0.dp`。 |
| defaultMinWidth | Dp | 弹窗的默认最小宽度。若设置为 `Dp.Unspecified`，则弹窗的宽度由内容决定（即“包裹内容”）。默认值为 `160.dp`。 |
| defaultMinHeight | Dp | 弹窗的默认最小高度。若设置为 `Dp.Unspecified`，则弹窗的高度由内容决定。默认值为 `0.dp`。 |
| properties | PopupProperties | 行为属性集，用于精细控制弹窗的行为，例如： ;; * `focusable`：弹窗是否可以获得焦点。 ;  * `dismissOnClickOutside`：点击弹窗的外部区域后，是否将其关闭。 ;  * `excludeFromSystemGesture`：是否排除系统手势。 |
| content | @Composable () -> Unit | 弹窗中的内容。你可以放置需要在弹窗内显示的任何 Compose UI。 |
## 使用限制
不支持自定义弹窗在空间中的浮起高度。
## 基础用法
以下代码展示了如何通过状态控制一个 `SpatialPopup` 的显示与隐藏，并以 `Button` 作为触发锚点，当用户点击按钮时在空间中弹出一个可被关闭的空间弹窗。
```Kotlin
@Composable
fun SpatialPopupSample() {
    // 声明空间弹窗的显示状态
    var showPopup by remember { mutableStateOf(false) }
    Box {
        // 声明一个空间弹窗
        if (showPopup) {
            SpatialPopup(
                onDismissRequest = {
                    // 关闭弹窗
                    showPopup = false
                }
            ) {
                // 弹窗中的内容
                Text(text = "SpatialPopup", modifier = Modifier.align(Alignment.Center))
            }
        }
        // 使用 Button 作为弹窗的锚点
        Button(
            onClick = {
                // 显示弹窗
                showPopup = true
            }
        ) {
            Text("show popup")
        }
    }
}
```

## 高阶用法
## 关于锚点 View
SpatialPopup 是基于某个 View 的空间位置进行弹出的。该 View 作为锚点 View，即 SpatialPopup 在布局和空间定位时所依附的父级 View。
例如，在下面的代码中，`Column` 即为 `SpatialPopup` 的锚点 View
```Kotlin
Row {
    Column {
        SpatialPopup()
    }
}
```


* **锚点 View 的 Padding 对 Popup 对齐的影响**
   锚点 View 上的 `padding` 会直接影响 SpatialPopup 的对齐逻辑。SpatialPopup 的对齐区域并不是基于锚点 View 的可见尺寸，而是基于扣除 `padding` 后的实际内容区域。
   如下示例中，`Box` 的整体尺寸为 100 dp（红色区域），但由于设置了 `padding(20.dp)`，真正作为 SpatialPopup 锚点的区域是黄色部分的 60 dp，而不是红色区域。

   ```Kotlin
   Box(modifier = Modifier
       .size(100.dp)
       .background(Color.Red)
       .padding(20.dp)
       .background(Color.Yellow)
   ) {
       SpatialPopup()
   }
   ```


   组件库中的多数组件（如 `Button`、`IconButton` 等）内部默认带有 padding。当直接使用这些组件作为 SpatialPopup 的锚点时，可能会出现视觉上无法对齐的情况。
   **推荐做法**：
   将 `Button` 与 `SpatialPopup` 放置在同一个 `Box` 中，由 `Box` 作为锚点 View，从而避免 padding 对对齐造成影响。
* **锚点 View 的子 View 对锚点区域的影响**
   锚点 View 内部的其他子 View 也会影响锚点区域的尺寸，因此在锚点 View 中放置额外的子 View 时需要特别谨慎。
   例如，在以下代码中，由于 `CustomView` 使用了 `fillMaxSize`，导致 `Box` 被撑满，最终使得 SpatialPopup 无法与 `Button` 正确对齐。
   ```Kotlin
   Box {
       CustomView(modifier = Modifier.fillMaxSize)
       var showSpatialPopup by remember {mutableStateOf(false)}
       Button() {
           Text("show SpatialPopup")
       }
       if(showSpatialPopup) {
           SpatialPopup()
       }
   }
   ```

   **推荐做法**：
   `Box` 上不要使用任何关于 Size 的 Modifier**，**使用 `Box` 承载目标 View（如 `Button`） 和 SpatialPopup。`Box` 内除了目标 View 和 SpatialPopup 外，不要放置其它 View。如下：
   ```Kotlin
   Box {
       // 可以是Button，或者是其他组件
       Button() {}
       // 相对于Button的位置弹出菜单
       SpatialPopup()
      
   }
   ```


### 自定义弹窗的弹出位置
Spatial UI 为 SpatialPopup 提供了一套基于锚点 View 的位置排布规则，用于描述弹窗相对于锚点（如 `Button`）在空间中的显示位置。弹出位置由水平方向（Horizontal）和垂直方向（Vertical）两个维度共同决定。

水平方向的排布规则：

垂直方向的排布规则：

在实际使用中，你可以通过 `rememberSpatialPopupPositionProvider`，结合 `HorizontalPlacement` 和 `VerticalPlacement`，来自定义 SpatialPopup 的弹出位置。
此外，在不改变整体排布规则的前提下，你可以使用 `offset` 对 SpatialPopup 的最终显示位置进行精确控制。`offset` 的取值遵循 View 的本地坐标系定义。
```Kotlin
popupPositionProvider = rememberSpatialPopupPositionProvider(
    horizontalPlacement = HorizontalPlacement.toStartOf(offset = -8.dp),
    verticalPlacement = VerticalPlacement.alignBottom
)
```


以下代码通过自定义 `popupPositionProvider`，将 SpatialPopup 设置为相对于锚点 View 左对齐并显示在其下方一定距离处，并通过状态控制实现弹窗的显示与关闭。
```Kotlin
@Composable
fun CustomPopupPositionSample() {
    // 声明空间弹窗的显示状态
    var showPopup by remember { mutableStateOf(false) }
    Box {
        if (showPopup) {
            SpatialPopup(
                // 自定义 SpatialPopup 的弹出位置
                popupPositionProvider = rememberSpatialPopupPositionProvider(
                    horizontalPlacement = HorizontalPlacement.alignStart(),
                    verticalPlacement = VerticalPlacement.below(offset = 10.dp)
                ),
                onDismissRequest = { showPopup = false },
            ) {
                Text(text = "SpatialPopup", modifier = Modifier.align(Alignment.Center))
            }
        }
        Button(onClick = { showPopup = true }) { Text("show popup") }
    }
}
```


### 使弹窗自适应内容的尺寸
默认情况下，SpatialPopup 会使用预设的最小尺寸进行布局。通过将 `defaultMinWidth` 和 `defaultMinHeight` 设置为 `Dp.Unspecified`，可以让弹窗尺寸根据其内部内容自动调整，从而实现自适应内容大小的显示效果。
```Kotlin
@Composable
fun SpatialPopupWrapContentSizeSample() {
    var showPopup by remember { mutableStateOf(false) }
    Box {
        if (showPopup) {
            SpatialPopup(
                // 使用 Dp.Unspecified 来包裹（自适应）内容尺寸
                defaultMinHeight = Dp.Unspecified,
                defaultMinWidth = Dp.Unspecified,
                onDismissRequest = { showPopup = false },
            ) {
                Text(text = "SpatialPopup", modifier = Modifier.align(Alignment.Center))
            }
        }
        Button(onClick = { showPopup = true }) { Text("show popup") }
    }
}
```

