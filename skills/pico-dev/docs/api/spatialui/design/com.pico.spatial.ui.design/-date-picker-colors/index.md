# DatePickerColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / DatePickerColors 
# DatePickerColors
```kotlin
@Immutable
```class  DatePickerColors 
colors for  DatePicker 
Members 
## Properties
inactive Date Color 
```kotlin
val inactiveDateColor: Color
```
Color for inactive date text. 
primary Content Color 
```kotlin
val primaryContentColor: Color
```
Main text color for date and title. 
range Background Color 
```kotlin
val rangeBackgroundColor: Color
```
Color for rang selection. 
selected Date Background Color 
```kotlin
val selectedDateBackgroundColor: Color
```
Color for selected date. 
today Background Color 
```kotlin
val todayBackgroundColor: Color
```
Background color for today. 
today Text Color 
```kotlin
val todayTextColor: Color
```
Color for today text. 
week Text Color 
```kotlin
val weekTextColor: Color
```
Color for week title. 
## Functions
copy 
```kotlin
fun copy(primaryContentColor: Color = this.primaryContentColor, weekTextColor: Color = this.weekTextColor, inactiveDateColor: Color = this.inactiveDateColor, selectedDateBackgroundColor: Color = this.selectedDateBackgroundColor, todayBackgroundColor: Color = this.todayBackgroundColor, todayTextColor: Color = this.todayTextColor, rangeBackgroundColor: Color = this.rangeBackgroundColor): DatePickerColors
```equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```