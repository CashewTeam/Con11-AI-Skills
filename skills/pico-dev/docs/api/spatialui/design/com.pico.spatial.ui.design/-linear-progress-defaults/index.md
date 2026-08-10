# LinearProgressDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / LinearProgressDefaults 
# LinearProgressDefaults
```kotlin
object LinearProgressDefaults
```
Default values for  LinearProgressIndicator 
Members 
## Properties
Regular 
```kotlin
val Regular: LinearProgressHeight
```
A pre-defined size of  LinearProgressIndicator 
Small 
```kotlin
val Small: LinearProgressHeight
```
A pre-defined size of  LinearProgressIndicator 
## Functions
linear Progress Colors 
```kotlin
@Composable
```fun  linearProgressColors ( ) :  ProgressColors 
The default colors used for  LinearProgressIndicator 
```kotlin
@Composable
```fun  linearProgressColors ( indicatorColor :  Color  =  Color.Unspecified ,  backgroundColor :  Color  =  Color.Unspecified ) :  ProgressColors 
custom colors for linear progress indicator 
linear Progress Height 
```kotlin
fun linearProgressHeight(value: Dp = Dp.Unspecified): LinearProgressHeight
```
custom size for  LinearProgressIndicator