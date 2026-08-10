Chip 是 PICO 设计规范下常用于标签展示场景下的控件，根据样式与功能不同，包含了 ButtonChip、ToggleableChip 以及 RemovableChip。
## ButtonChip
ButtonChip 是 PICO 设计规范下用于展示标签的控件，通常用于在标签展示场景中提供内容与响应内容点击。

### API Surface

* `label`：当前 ButtonChip 的文本内容，是一个 Composable。
* `onClick`：点击事件，当 ButtonChip 被点击时会响应此回调。
* `leadingIcon`：可用于自定义添加控件，配置 ButtonChip 左侧内容展示，默认情况下不展示。
* `trailingIcon`：可用于自定义添加控件，配置 ButtonChip 右侧内容展示，默认情况下不展示。
* `enabled`：是否响应用户的悬停手势，布尔值。默认为 true，用户在 ButtonChip 控件悬停时具有默认的 hover 效果。
* `labelTextStyle`：用于控制 `label` 的文字展示风格，默认为 `PicoTheme.typography.labelLarge`。
* `colors`：用于提供当前 `label`、`leadingIcon`、`trailingIcon` 与 ButtonChip 的背景颜色，默认由 `ChipsDefaults.chipColors` 提供，也可以通过 `ChipsDefaults.chipColors` 传递自定义颜色。
* `chipSize`：用于控制 ButtonChip 的大小，默认情况下样式为 `ChipsDefaults.Small`。
* `interactionSource`：用于监听 ButtonChip 交互状态改变，可以提供自定义的 `MutableInteractionSource` 来监听控件的按下、聚焦等交互状态。

### 基础用法
```Kotlin
@Composable
fun ButtonChipSample() {
    Column {
        // 展示标签
        ButtonChip(label = {
          Text("Chip")
        }, onClick = {})
    }
}
```


### **高阶用法**
自定义 ButtonChip，通过自定义 `leadingIcon`、`trailingIcon`、`chipSize` 等，可以实现丰富的 ButtonChip 展示效果。
```Kotlin
@Composable
fun ButtonChipsDemo(){
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        ButtonChip(
            label = {
             Text("Complex")
            },
            onClick = {},
            chipSize = ChipsDefaults.Small,
            // 左侧展示一个icon
            leadingIcon = {
                AnyIcon(iconSize = 12.dp)
            },
            // 右侧也展示文字
            trailingIcon = {
                Text("Right Text")
            },
            // 可以自定义label颜色，以及背景色
            colors = ChipsDefaults.chipColors(Color.Yellow, Color.Black)
        )
    }
}
```


## ToggleableChip
ToggleableChip 是 PICO 设计规范下可用于切换状态的标签，区别于 ButtonChip，ToggleableChip 具备默认选中与非选中状态提示
### API Surface

* `label`：当前 ToggleableChip 的文本内容，是一个 Composable。
* `isToggleOn`：当前 ToggleableChip 是否处于选中状态。
* `onClick`：点击事件，当 ToggleableChip 被点击时会响应此回调。
* `leadingIcon`：可用于自定义添加控件，配置 ToggleableChip 左侧内容展示，默认情况下不展示。
* `trailingIcon`：可用于自定义添加控件，配置 ToggleableChip 右侧内容展示，默认情况下不展示。
* `enabled`：是否响应用户的悬停手势，布尔值。默认为 true，用户在 ToggleableChip 控件悬停时具有默认的 hover 效果。
* `labelTextStyle`：用于控制 `label` 的文字展示风格，默认为 `PicoTheme.typography.labelLarge`。
* `colors`：用于提供当前 `label`、`leadingIcon`、`trailingIcon` 以及 ToggleableChip 选中与非选中的颜色、ToggleableChip 的背景颜色，默认由 `ChipsDefaults.toggleableChipColors` 提供，也可以通过 `ChipsDefaults.toggleableChipColors` 传递自定义颜色。
* `chipSize`：用于控制 ToggleableChip 的大小，默认情况下样式为 `ChipsDefaults.Small`。
* `interactionSource`：用于监听 ToggleableChip 交互状态改变，可以提供自定义的 `MutableInteractionSource` 来监听控件的按下、聚焦等交互状态。

### 基础用法
```Kotlin
@Composable
fun ToggleableChipSample() {
    Column(modifier = Modifier.padding(12.dp)) {
        var selected by remember { mutableStateOf(false) }
        // 选中状态展示
        ToggleableChip(
            label = {
              Text("Chip 1")
            },
            isToggleOn = selected,
            onClick = { selected = !selected },
        )
        Spacer(modifier = Modifier.height(10.dp))
        // 非选中状态展示
        ToggleableChip(
            label = {
              Text("Chip 2")
            },
            isToggleOn = !selected,
            onClick = { selected = !selected },
        )
    }
}
```


### **高阶用法**
自定义 ToggleableChip，通过自定义 `leadingIcon`、`trailingIcon`、`chipSize` 以及 `colors` 等，可实现丰富的 ToggleableChip 展示效果。
```Kotlin
@Composable
fun ToggleableChipSample(){
    var selected by remember { mutableStateOf(false) }
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        ToggleableChip(
            label = {
               Text("Complex")
            },
            isToggleOn = selected,
            onClick = {selected = !selected},
            chipSize = ChipsDefaults.Small,
            // 左侧展示一个icon
            leadingIcon = {
                AnyIcon(iconSize = 12.dp)
            },
            // 右侧也展示文字
            trailingIcon = {
                Text("Right Text")
            },
            // 可以自定义label颜色，背景色.以及设置选中时颜色为Color.Red，选中时背景色为Color.Blue
            colors = ChipsDefaults.toggleableChipColors(Color.Yellow, Color.Black,Color.Red,Color.Blue)
        )
    }
}
```


## RemovableChip
RemovableChip 是 PICO 设计规范下可用于显示或者删除的动态标签，可用于自定义“删除”样式。
### API Surface

* `label` : 当前 RemovableChip 的文本内容，是一个 Composable。
* `onLeadingClick`：点击 `leadingIcon` 或者 `label` 等 leading 区域时的点击事件回调。
* `onTrailingRemoveClick`：点击右侧关闭按钮时的事件回调。
* `visible`：控制当前 RemovableChip 是否可见。
* `leadingIcon` : 可用于自定义添加控件，配置 RemovableChip 左侧内容展示，默认情况下不展示。
* `enabled` : 是否响应用户的悬停手势，布尔值。默认为 true，用户在 RemovableChip 控件悬停时具有默认的 hover 效果。
* `labelTextStyle` : 用于控制 `label` 的文字展示风格，默认为 `PicoTheme.typography.labelLarge`。
* `colors`：用于提供当前 `label`、`leadingIcon` 与 RemovableChip 的背景颜色，默认由 `ChipsDefaults.chipColors` 提供，也可以通过 `ChipsDefaults.chipColors` 传递自定义颜色。
* `chipSize`：用于控制 RemovableChip 的大小，默认情况下样式为 `ChipsDefaults.Small`。
* `contentPadding`：RemovableChip 显示的内容内边距，可通过传入 `PaddingValues` 对象自定义水平与垂直方向的内边距。
* `contentGap`：用于设置 `leadingIcon` 与 `label` 之间的间距。
* `shape`：用于设置 RemovableChip 的 shape 样式，内部内容会应用 shape 展示。
* `interactionSource`：用于监听 RemovableChip 交互状态改变，可以提供自定义的 `MutableInteractionSource` 来监听控件的按下、聚焦等交互状态。

### 基础用法
```Kotlin
@Composable
fun RemovableChipDemo(){
    var visible by remember {
        mutableStateOf(true)
    }
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        RemovableChip(
            label = {
             Text("RemovableChip")
            },
            // 点击右侧关闭按钮后隐藏RemovableChip
            onTrailingRemoveClick = {
                visible = !visible
            },
            // 点击右侧关闭按钮后隐藏RemovableChip
            onLeadingClick = {
                visible = !visible
            },
            visible = visible
        )
    }
}
```


### **高阶用法**
自定义 RemovableChip，通过自定义 `leadingIcon`、`contentPadding`、`contentGap` 以及 `shape` 等，可以实现丰富的 RemovableChip 展示效果。
```Kotlin
@Composable
fun RemovableChipDemo(){
    var visible by remember {
        mutableStateOf(true)
    }
    Box(contentAlignment = Alignment.Center, modifier = Modifier.fillMaxSize()) {
        RemovableChip(
            label = {
               Text("RemovableChip")
            },
            // 点击右侧关闭按钮后隐藏RemovableChip
            onTrailingRemoveClick = {
                visible = !visible
            },
            // 点击右侧关闭按钮后隐藏RemovableChip
            onLeadingClick = {
                visible = !visible
            },
            // 设置左侧展示icon
            leadingIcon = {
                AnyIcon(iconSize = 12.dp)
            },
            // 设置label与leadingIcon间距为10dp
            contentGap = 10.dp,
            // 设置水平与垂直内边距为10dp
            contentPadding = PaddingValues(10.dp,10.dp),
            visible = visible
        )
    }
}
```


