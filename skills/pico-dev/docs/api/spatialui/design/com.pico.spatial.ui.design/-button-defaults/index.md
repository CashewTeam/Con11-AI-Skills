# ButtonDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ButtonDefaults 
# ButtonDefaults
```kotlin
object ButtonDefaults
```
Object holding default values used by buttons 
Members 
## Properties
Max 
```kotlin
val Max: ButtonSize
```
A pre-defined size for buttons 
Min 
```kotlin
val Min: ButtonSize
```
A pre-defined size for buttons 
Regular 
```kotlin
val Regular: ButtonSize
```
A pre-defined size for buttons 
Small 
```kotlin
val Small: ButtonSize
```
A pre-defined size for buttons 
## Functions
button Colors 
```kotlin
@Composable
```fun  buttonColors ( ) :  ButtonColors 
Creates a default  ButtonColors  object with the accent color from the Pico theme as the container color and the on-accent color from the Pico theme as the content color. 
```kotlin
@Composable
```fun  buttonColors ( containerColor :  Color  =  Color.Unspecified ,  contentColor :  Color  =  Color.Unspecified ) :  ButtonColors 
Creates a  ButtonColors  that represents the default container and content colors used in a  Button . 
button Size 
```kotlin
fun buttonSize(width: Dp = Dp.Unspecified, height: Dp = Dp.Unspecified, minWidth: Dp = Dp.Unspecified, maxWidth: Dp = Dp.Unspecified, minHeight: Dp = Dp.Unspecified, maxHeight: Dp = Dp.Unspecified): ButtonSize
```
Creates a  ButtonSize  that presents sizes used by  Button