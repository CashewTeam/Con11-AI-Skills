NumberField 是在 PICO 设计规范下，允许用户创建一个带有增减按钮的数字输入框。

## API Surface

* `value`：数字字段的当前值。
* `onValueChange`：当 value 值发生变化时触发的回调。
* `increaseIcon`：增加按钮所显示的图标，默认由 `NumberFieldDefaults.defaultIncreaseIcon()` 方法提供样式。
* `decreaseIcon`：减少按钮所显示的图标，默认由 `NumberFieldDefaults.defaultDecreaseIcon()` 方法提供样式。
* `stepLength`：用于增大或减小数值的步长。
* `valueRange`：`value` 的有效取值范围。
* `colors`：设置 NumberField 的颜色，包括背景色、内容颜色等，默认由 `NumberFieldDefaults.numberFieldColors()` 方法提供。
* `size`：NumberField 的大小。
* `cornerSize`：NumberField 的边角尺寸。
* `gap`：`increaseIcon`、`value` 以及 `decreaseIcon` 之间的间距，默认由 `NumberFieldDefaults.DefaultGap` 提供。
* `enabled`：NumberField 是否启用，布尔值，默认为 true。
* `editable`：NumberField 是否可编辑，布尔值，默认为 true。
* `textStyle`：NumberField 的文本样式。
* `keyboardOptions`：NumberField 的键盘控制，默认输入数字，可自定义此内容控制其他键盘输入方式。

## 基础用法
```Kotlin
@Composable
fun NumberFieldSample() {
    var value by remember { mutableIntStateOf(0) }
    NumberField(value = value, onValueChange = { value = it })
}
```


## **高阶用法**

* 可以通过 `decreaseIcon` 与 `increaseIcon`，设置 NumberField 的图标展示。
* 可以通过 `stepLength` 设定每次 `value` 增加或者减少的步长，通过 `valueRange` 限定最终 `value` 的范围。

```Kotlin
@Composable
fun NumberFieldStepLengthSample() {
    Column {
        Text("Custom Step + 2")
        var value by remember { mutableIntStateOf(0) }
        // 修改增加删除icon为自定义icon，设置step为2，范围为-10～10，观察按钮表现
        NumberField(value = value, onValueChange = { value = it }, stepLength = 2, decreaseIcon = {
            AnyIcon()
        }, increaseIcon = {
            AnyIcon()
        }, valueRange = IntRange(-10,10))
    }
}
```


