# WheelPickerColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / WheelPickerColors 
# WheelPickerColors
```kotlin
@Immutable
```class  WheelPickerColors 
Define colors for  WheelPicker 
Members 
## Properties
item Text Color 
```kotlin
val itemTextColor: Color
```
The text color of normal item. 
selected Indicator Color 
```kotlin
val selectedIndicatorColor: Color
```
The background color of selected item. 
selected Text Color 
```kotlin
val selectedTextColor: Color
```
The text color of selected item. 
## Functions
copy 
```kotlin
fun copy(selectedTextColor: Color = this.selectedTextColor, selectedIndicatorColor: Color = this.selectedIndicatorColor, itemTextColor: Color = this.itemTextColor): WheelPickerColors
```equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```