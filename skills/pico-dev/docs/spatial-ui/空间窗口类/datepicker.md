本文介绍 DatePicker、DateRangePicker 组件的能力和用法。
## DatePicker
DatePicker 是在 PICO 设计规范下，可用于进行日期选择的控件。

### API Surface

* `onDateSelected`：当日期被选中时调用的回调函数。
* `state`：DatePicker 的状态。可以自定义 rememberDatePickerState，用于监听 DatePicker 内部状态变化。
* `dateFormatter`：DatePicker 格式化器，它提供日期显示的格式化框架，并将其转换为日期输入。
* `colors`：DatePicker 颜色，用于解析此日期选择器在不同状态下使用的颜色，默认由 `DatePickerDefaults.datePickerColors()` 提供。
* `headerStyle`：控制 DatePicker 的头部样式。

### 基础用法
```Kotlin
@Preview
@Composable
fun DatePickerCannotSwitchYearSample() {
    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
        var millis: Long? by remember { mutableStateOf(null) }
        // 通过onDateSelected拿到当前日期
        DatePicker(
            onDateSelected = { millis = it },
        )
        Text("Selected date: ${millis.formatToText()} ", color = Color.Black)
    }
}
```


### **高阶用法**

* 可通过 `headerStyle` 修改，可以选择其他的年份设置样式。
* 通过提高 `rememberDatePickerState` 提供 `state`，可以默认选中其他的日期达到自定义效果。

```Kotlin
@Composable
fun DatePickerCannotSwitchYearSample() {
    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
        var millis: Long? by remember { mutableStateOf(null) }
        DatePicker(
            onDateSelected = { millis = it },
            headerStyle = HeaderStyle.Dropdown,
            // 提供默认的开始时间
            state = rememberDatePickerState(initialSelectedDateMillis = 1740693600000)
        )
        Text("Selected date: ${millis.formatToText()} ", color = Color.Black)
    }
```


## DateRangePicker
DateRangePicker 是在 PICO 设计规范下，可用于选中一段时间的组件。
### API Surface

* `onStartSelected`：当开始日期被选中时调用的回调函数。
* `onEndSelected`：当结束日期被选中时调用的回调函数。
* `state`：DateRangePicker 的状态。可以自定义 rememberDateRangePickerState，用于监听 DateRangePicker 内部状态变化
* `dateFormatter`：DateRangePicker 格式化器，它提供日期显示的格式化框架，并将其转换为日期输入。
* `colors`：DateRangePicker 颜色，用于解析此日期选择器在不同状态下使用的颜色，默认由`DatePickerDefaults.datePickerColors()` 提供
* `headerStyle`：控制 DateRangePicker 的头部样式。

### 基础用法
```Kotlin
@Composable
fun DateRangePickerSample() {
    var start: Long? by remember { mutableStateOf(null) }
    var end: Long? by remember { mutableStateOf(null) }
    Column(modifier = Modifier.fillMaxSize(), verticalArrangement = Arrangement.Top) {
        DateRangePicker(
            onStartSelected = { start = it },
            onEndSelected = { end = it },
        )
        Text(
            "Selected date range: ${start.formatToText()} -- ${end.formatToText()}",
            color = Color.Black
        )
    }
}
```


### **高阶用法**
可以通过 headerStyle 修改，可以选择其他的年份设置样式，修改 color 自定义选中颜色等。
```Kotlin
/** DateRangePickerSample */
@Preview
@Composable
fun DateRangePickerSample() {
    var start: Long? by remember { mutableStateOf(null) }
    var end: Long? by remember { mutableStateOf(null) }
    Column(modifier = Modifier.fillMaxSize(), verticalArrangement = Arrangement.Top) {
        DateRangePicker(
            headerStyle = HeaderStyle.Dropdown,
            onStartSelected = { start = it },
            onEndSelected = { end = it },
        )
        Text(
            "Selected date range: ${start.formatToText()} -- ${end.formatToText()}",
            color = Color.Black
        )
    }
}
```


