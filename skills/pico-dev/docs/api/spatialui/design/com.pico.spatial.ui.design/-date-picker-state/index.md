# DatePickerState | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / DatePickerState 
# DatePickerState
```kotlin
@Stable
```interface  DatePickerState 
A state object that can be hoisted to observe the date picker state. See  rememberDatePickerState . 
Members 
## Properties
displayed Month Millis 
```kotlin
abstract var displayedMonthMillis: Long
```
A timestamp that represents the currently displayed month  start  date in  UTC  milliseconds from the epoch. 
selected Date Millis 
```kotlin
abstract var selectedDateMillis: Long?
```
A timestamp that represents the selected date  start  of the day in  UTC  milliseconds from the epoch.