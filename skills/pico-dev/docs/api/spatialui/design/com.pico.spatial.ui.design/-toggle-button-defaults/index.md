# ToggleButtonDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ToggleButtonDefaults 
# ToggleButtonDefaults
```kotlin
object ToggleButtonDefaults
```
Contains the default values used by  ToggleButton 
Members 
## Properties
Max 
```kotlin
val Max: ButtonSize
```
A pre-defined size for toggle button 
Min 
```kotlin
val Min: ButtonSize
```
A pre-defined size for toggle button 
Regular 
```kotlin
val Regular: ButtonSize
```
A pre-defined size for toggle button 
Small 
```kotlin
val Small: ButtonSize
```
A pre-defined size for toggle button 
## Functions
toggle Button Colors 
```kotlin
@Composable
```fun  toggleButtonColors ( ) :  ToggleButtonColors 
```kotlin
@Composable
```fun  toggleButtonColors ( checkedContainerColor :  Color  =  Color.Unspecified ,  checkedContentColor :  Color  =  Color.Unspecified ,  uncheckedContainerColor :  Color  =  Color.Unspecified ,  uncheckedContentColor :  Color  =  Color.Unspecified ) :  ToggleButtonColors 
The content color will effect both ToggleButton's leading and trailing icon and content 
toggle Button Size 
```kotlin
fun toggleButtonSize(width: Dp = Dp.Unspecified, height: Dp = Dp.Unspecified, minWidth: Dp = Dp.Unspecified, maxWidth: Dp = Dp.Unspecified, minHeight: Dp = Dp.Unspecified, maxHeight: Dp = Dp.Unspecified): ButtonSize
```
Creates a  ButtonSize  that presents sizes used by  ToggleButton