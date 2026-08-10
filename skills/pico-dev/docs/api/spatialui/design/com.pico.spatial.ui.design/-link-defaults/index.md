# LinkDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / LinkDefaults 
# LinkDefaults
```kotlin
object LinkDefaults
```
Holds the default values used by  Link . 
Members 
## Properties
Max 
```kotlin
val Max: ButtonSize
```
A Built-in  ButtonSize s for  Link . 
Regular 
```kotlin
val Regular: ButtonSize
```
A Built-in  ButtonSize s for  Link . 
## Functions
button Size 
```kotlin
fun buttonSize(width: Dp = Dp.Unspecified, height: Dp = Dp.Unspecified, minWidth: Dp = Dp.Unspecified, maxWidth: Dp = Dp.Unspecified, minHeight: Dp = Dp.Unspecified, maxHeight: Dp = Dp.Unspecified): ButtonSize
```
Creates a  ButtonSize  that presents sizes used by  Link 
default Colors 
```kotlin
@Composable
```fun  defaultColors ( ) :  ButtonColors link Colors 
```kotlin
@Composable
```fun  linkColors ( containerColor :  Color  =  Color.Unspecified ,  contentColor :  Color  =  Color.Unspecified ) :  ButtonColors 
Creates a  ButtonColors  that represents the default container and content colors used in a  Link .