ToggleButton 是 PICO 设计规范下，一种带有二级“状态”的用于响应用户点击交互的控件，内容区域通常为 `Text`， 或其他可组合项，常用于新建、添加等场景，可设置 leading、trailing 的图标。

## API Surface

* `checked`：是否被选中。
* `onCheckedChange`：触发改变状态的回调。
* `enabled`：是否可用，布尔值。
* `size`：控件的尺寸，可通过 `ToggleIconButtonDefaults` 方法进行自定义，取值为 `Min` 表示使用默认尺寸。
* `colors`：控件的颜色， 可通过 `ToggleIconButtonDefaults` 方法自定义 `checkedContainerColor`、`checkedContainerColor`、`checkedContainerColor`、`checkedContainerColor`。
* `leadingIcon`：`@Composable` 回调函数，显示首部图标，可选。
* `trailingIcon`：`@Composable` 回调函数，显示尾部图标， 可选。
* `contentPadding`：内容的内边距， 默认值使用 `ButtonDefaults` 方法设置。
* `shape`：控件的形状， 可自定义， 默认值使用 `ButtonDefaults` 方法设置。
* `gap`：图标与内容之间的间距。仅在使用 `MutableInteractionSource` 调用 `leadingIcon` 和 `trailingIcon` 配置时才会生效。
* `content`：控件的内容， 通常为`Text`。

## 基础用法
```Kotlin
/** A simple toggle button */
@Composable
fun ToggleButtonSample() {
    var isChecked by remember { mutableStateOf(false) }
    ToggleButton(isChecked, onCheckedChange = { isChecked = it }) { Text("ToggleButton") }
}
```


## 高阶用法

* 自定义 ToggleButton 的尺寸、形状、颜色、首部、尾部、内容间距、标题和图标之间的间距，可用于选中、非选中状态的切换场景。

   ```Kotlin
   @Composable
   fun ToggleButtonSample() {
       var isChecked by remember { mutableStateOf(false) }
       ToggleButton(
           isChecked,
           onCheckedChange = { isChecked = !isChecked },
           //自定义颜色
           colors = ToggleButtonDefaults.toggleButtonColors(
               checkedContainerColor = Color(color = 0xFF3D8BFF),
               checkedContentColor = Color(color = 0xFFFFFFFF),
               uncheckedContainerColor = Color.Black,
               uncheckedContentColor = Color(color = 0xFFFFFFFF)
           ),
           //自定义大小
           size = ToggleButtonDefaults.toggleButtonSize(width = 150.dp, height = 40.dp),
           //自定义形状
           shape = RoundedCornerShape(20.dp),
           //内容边距
           contentPadding = PaddingValues(10.dp),
           //标题和图标之间的间距
           gap = 10.dp,
           //自定义首部图标， 可选
           leadingIcon = { AnyIcon(iconSize = 22.dp) },
           //自定义尾部图标， 可选
           trailingIcon = { AnyIcon(iconSize = 22.dp) }
       ) {
           Text( if (isChecked) "Selected" else "Unselected")
       }
   }
   ```

* ToggleButton 实现类似 DropDown Trigger 示例。

   ```Kotlin
   @Composable
   fun ToggleButtonDropdownSample(){
       var isChecked by remember { mutableStateOf(false) }
       Box {
           ToggleButton(
               checked = isChecked,
               onCheckedChange = { isChecked = !isChecked },
               colors = ToggleButtonDefaults.toggleButtonColors(
                   checkedContainerColor = PicoTheme.colorScheme.onAccent,
                   checkedContentColor = PicoTheme.colorScheme.accent,
                   uncheckedContainerColor = Color(0x0A7F7F7F),
                   uncheckedContentColor = PicoTheme.colorScheme.accent
               ),
               trailingIcon = {
                   Icon(
                       modifier = Modifier.size(16.dp),
                       painter =
                       painterResource(
                          id = R.drawable.sample_icon_down
                       ),
                       contentDescription = null
                   )
               }
           ) {
               Text("Value")
           }
           if (isChecked) {
               Menu(onDismissRequest = { isChecked = false }) {
                   MenuItem(title = { Text("Option 1") })
                   MenuItem(title = { Text("Option 2") })
                   MenuItem(title = { Text("Option 3") })
               }
           }
       }
   }
   ```

