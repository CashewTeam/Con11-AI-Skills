# IconButtonDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / IconButtonDefaults 
# IconButtonDefaults
```kotlin
object IconButtonDefaults
```
Holding IconButton default values. 
Members 
## Properties
Max 
```kotlin
val Max: ButtonSize
```
A pre-defined size of  IconButton 
Min 
```kotlin
val Min: ButtonSize
```
A pre-defined size of  IconButton 
Regular 
```kotlin
val Regular: ButtonSize
```
A pre-defined size of  IconButton 
Small 
```kotlin
val Small: ButtonSize
```
A pre-defined size of  IconButton 
## Functions
icon Button Colors 
```kotlin
@Composable
```fun  iconButtonColors ( ) :  ButtonColors 
Default  ButtonColors  for  IconButton  follow PicoTheme 
```kotlin
@Composable
```fun  iconButtonColors ( containerColor :  Color  =  Color.Unspecified ,  contentColor :  Color  =  Color.Unspecified ) :  ButtonColors 
Creates a  ButtonColors  that represents the default container and content colors used in a  IconButton . 
icon Button Size 
```kotlin
fun iconButtonSize(size: Dp): ButtonSize
```
```kotlin
fun iconButtonSize(width: Dp, height: Dp): ButtonSize
```
```kotlin
fun iconButtonSize(width: Dp = Dp.Unspecified, height: Dp = Dp.Unspecified, minWidth: Dp = Dp.Unspecified, maxWidth: Dp = Dp.Unspecified, minHeight: Dp = Dp.Unspecified, maxHeight: Dp = Dp.Unspecified): ButtonSize
```
Creates a  ButtonSize  that presents sizes used by  IconButton