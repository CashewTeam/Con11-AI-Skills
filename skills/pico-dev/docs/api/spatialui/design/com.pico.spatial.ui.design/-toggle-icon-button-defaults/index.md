# ToggleIconButtonDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ToggleIconButtonDefaults 
# ToggleIconButtonDefaults
```kotlin
object ToggleIconButtonDefaults
```
Holding ToggleIconButton default values. 
Members 
## Properties
Max 
```kotlin
val Max: ButtonSize
```
A pre-defined size of  ToggleIconButton 
Min 
```kotlin
val Min: ButtonSize
```
A pre-defined size of  ToggleIconButton 
Regular 
```kotlin
val Regular: ButtonSize
```
A pre-defined size of  ToggleIconButton 
Small 
```kotlin
val Small: ButtonSize
```
A pre-defined size of  ToggleIconButton 
## Functions
toggle Icon Button Colors 
```kotlin
@Composable
```fun  toggleIconButtonColors ( ) :  ToggleButtonColors 
```kotlin
@Composable
```fun  toggleIconButtonColors ( checkedContainerColor :  Color  =  Color.Unspecified ,  checkedContentColor :  Color  =  Color.Unspecified ,  uncheckedContainerColor :  Color  =  Color.Unspecified ,  uncheckedContentColor :  Color  =  Color.Unspecified ) :  ToggleButtonColors 
The content color will effect both ToggleButton's leading and trailing icon and content 
toggle Icon Button Size 
```kotlin
fun toggleIconButtonSize(size: Dp): ButtonSize
```
```kotlin
fun toggleIconButtonSize(width: Dp, height: Dp): ButtonSize
```
Creates a  ButtonSize  that presents sizes used by  IconButton