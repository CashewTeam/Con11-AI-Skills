# DateRangePickerState | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / DateRangePickerState 
# DateRangePickerState
```kotlin
@Stable
```interface  DateRangePickerState 
A state object that can be hoisted to observe the date range picker state. See  rememberDateRangePickerState . 
Members 
## Properties
displayed Month Millis 
```kotlin
abstract var displayedMonthMillis: Long
```
A timestamp that represents the currently displayed month  start  date in  UTC  milliseconds from the epoch. 
selected End Date Millis 
```kotlin
abstract val selectedEndDateMillis: Long?
```
A timestamp that represents the selected end date  start  of the day in  UTC  milliseconds from the epoch. 
selected Start Date Millis 
```kotlin
abstract val selectedStartDateMillis: Long?
```
A timestamp that represents the selected start date  start  of the day in  UTC  milliseconds from the epoch. 
## Functions
set Selection 
```kotlin
abstract fun setSelection(startDateMillis: Long?, endDateMillis: Long?)
```
Sets a start and end selection dates.