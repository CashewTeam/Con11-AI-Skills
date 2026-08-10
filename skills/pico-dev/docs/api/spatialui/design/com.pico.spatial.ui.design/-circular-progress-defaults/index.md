# CircularProgressDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / CircularProgressDefaults 
# CircularProgressDefaults
```kotlin
object CircularProgressDefaults
```
Default values for  CircularProgressIndicator 
Members 
## Properties
Max 
```kotlin
val Max: CircularProgressSize
```
Max, A predefine size spec for circular indicator 
Regular 
```kotlin
val Regular: CircularProgressSize
```
Regular, A predefine size spec for circular indicator 
Small 
```kotlin
val Small: CircularProgressSize
```
Small, A predefine size spec for circular indicator 
## Functions
circle Progress Colors 
```kotlin
@Composable
```fun  circleProgressColors ( ) :  ProgressColors 
default colors for circular progress indicator 
```kotlin
@Composable
```fun  circleProgressColors ( backgroundColor :  Color  =  Color.Unspecified ,  indicatorColor :  Color  =  Color.Unspecified ) :  ProgressColors 
custom colors for  CircularProgressIndicator 
circle Progress Size 
```kotlin
fun circleProgressSize(size: Dp = Dp.Unspecified): CircularProgressSize
```
custom size for  CircularProgressSize