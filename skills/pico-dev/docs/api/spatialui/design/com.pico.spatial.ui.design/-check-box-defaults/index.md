# CheckBoxDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / CheckBoxDefaults 
# CheckBoxDefaults
```kotlin
object CheckBoxDefaults
```
Contains the default values used by CheckBox 
Members 
## Properties
Border Width 
```kotlin
val BorderWidth: Dp
```
border width of check box 
Checkbox Size 
```kotlin
val CheckboxSize: Dp
```
size of check box 
Regular 
```kotlin
val Regular: CheckboxContentSize
```
A pre-defined size for check box 
Regular Checkbox Content Size 
```kotlin
val RegularCheckboxContentSize: Dp
```
regular content size of check box 
Small 
```kotlin
val Small: CheckboxContentSize
```
A pre-defined size for check box 
Small Checkbox Content Size 
```kotlin
val SmallCheckboxContentSize: Dp
```
small content size of check box 
## Functions
checkbox Colors 
```kotlin
@Composable
```fun  checkboxColors ( ) :  CheckboxColor 
the default colors from the theme's color scheme of checkbox . 
```kotlin
@Composable
```fun  checkboxColors ( backgroundColor :  Color  =  Color.Unspecified ,  contentColor :  Color  =  Color.Unspecified ,  borderColor :  Color  =  Color.Unspecified ) :  CheckboxColor 
Creates a  CheckboxColor  that represents the default container and content colors used in a  Checkbox . 
check Box Size 
```kotlin
fun checkBoxSize(value: Dp = Dp.Unspecified): CheckboxContentSize
```
Creates a  CheckboxContentSize  that presents sizes used by  Checkbox