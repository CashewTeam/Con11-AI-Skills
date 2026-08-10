# PageControlDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / PageControlDefaults 
# PageControlDefaults
```kotlin
object PageControlDefaults
```
The default values of  PageControl . 
Members 
## Properties
Normal Max 
```kotlin
const val NormalMax: Int = 9
```
The maximum number of PageControl that can be displayed at the same time. 
Progress Max 
```kotlin
const val ProgressMax: Int = 16
```
The maximum number of ProgressPageControl that can be displayed at the same time. 
Spec 
```kotlin
val Spec: PageControlSpec
```
The default  PageControlSpec  used by  PageControl . 
## Functions
page Control Colors 
```kotlin
@Composable
```fun  pageControlColors ( ) :  PageControlColors 
The default colors used for  PageControl 
```kotlin
@Composable
```fun  pageControlColors ( highLightColor :  Color  =  Color.Unspecified ,  normalColor :  Color  =  Color.Unspecified ) :  PageControlColors 
Customize  PageControlColors  used for  PageControl . 
page Control Spec 
```kotlin
fun pageControlSpec(dotRadius: Dp = Dp.Unspecified, dotSpace: Dp = Dp.Unspecified, verticalPadding: Dp = Dp.Unspecified): PageControlSpec
```
Customize  PageControlSpec  used for  PageControl .