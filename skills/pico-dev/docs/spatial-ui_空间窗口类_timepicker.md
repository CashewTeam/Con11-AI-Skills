TimePicker 是在 PICO 设计规范下，进行时间纬度（时、分、秒）选择的控件。

## API Surface

* `config`：用于定义将显示哪些元素的配置，可以配置时分秒的显示。
* `onHoursChanged`：选中小时发生变化时将被调用。
* `onMinutesChanged`：选中分钟发生变化时将被调用。
* `onSecondsChanged`：选中秒发生变化时将被调用。
* `gap`：每个元素之间的间距，默认值由 `TimepickerDefaults.DefaultGap` 提供。
* `colors`：用于自定义选择器外观的滚轮选择器颜色，默认值由 `WheelPickerDefaults.wheelPickerColors()` 提供。

## 基础用法
```Kotlin
@Composable
private fun HMSPicker() {
    Column {
        Text(text = "Single time picker to select hour/minutes/seconds")
        var hour by remember { mutableStateOf("") }
        var sec by remember { mutableStateOf("") }
        var min by remember { mutableStateOf("") }
        Text(
            modifier = Modifier.padding(start = 10.dp),
            text = "Current result = $hour:$min$sec",
            style = PicoTheme.typography.labelMedium
        )

        Timepicker(
            onHoursChanged = { hour = it.toString() },
            onMinutesChanged = { min = it.toString() },
            onSecondsChanged = { sec = it.toString() }
        )
    }
}
```


## **进阶用法**

* 可通过 `TimepickerConfig.create` 方法自定义配置 `config`，显示时、分、秒中的选项以及选项文案。
* 可通过 `WheelPickerDefaults.wheelPickerColors()` 方法提供 `colors` 修改默认颜色。

```Kotlin
@Composable
private fun HMPicker() {
    Column {
        Text(text = "Single time picker to select hour/minutes/seconds")
        var hour by remember { mutableStateOf("") }
        var sec by remember { mutableStateOf("") }
        var min by remember { mutableStateOf("") }
        Text(
            modifier = Modifier.padding(start = 10.dp),
            text = "Current result = $hour:$min$sec",
            style = PicoTheme.typography.labelMedium
        )

        // 只显示小时和分钟，小时显示后添加h，分钟显示后添加m
        val ele = remember {
            TimepickerConfig.create(
                TimepickerElement.hours("h"),
                TimepickerElement.minutes("m"),
            )
        }
        Timepicker(
            config = ele,
            onHoursChanged = { hour = it.toString() },
            onMinutesChanged = { min = it.toString() },
            onSecondsChanged = { sec = it.toString() }
        )
    }

}
```


