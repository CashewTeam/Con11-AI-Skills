# SliderDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / SliderDefaults 
# SliderDefaults
```kotlin
object SliderDefaults
```
Object hold default values used by sliders 
Members 
## Properties
Max 
```kotlin
val Max: SliderSpec
```
A pre-defined size for Sliders 
Regular 
```kotlin
val Regular: SliderSpec
```
A pre-defined size for Sliders 
Small 
```kotlin
val Small: SliderSpec
```
A pre-defined size for Sliders 
## Functions
slider Colors 
```kotlin
@Composable
```fun  sliderColors ( ) :  SliderColors 
The default colors used for  Slider 
```kotlin
@Composable
```fun  sliderColors ( trackColor :  Color  =  Color.Unspecified ,  progressColor :  Color  =  Color.Unspecified ,  progressHighColor :  Color  =  Color.Unspecified ,  thumbColor :  Color  =  Color.Unspecified ,  thumbHighColor :  Color  =  Color.Unspecified ,  segmentDotColor :  Color  =  Color.Unspecified ) :  SliderColors 
Creates a  SliderColors  object for sliders. 
slider Spec 
```kotlin
fun sliderSpec(thumbAreaSize: Dp = Dp.Unspecified, thumbSize: Dp = Dp.Unspecified, thumbPressedSize: Dp = Dp.Unspecified, thumbHoverSize: Dp = Dp.Unspecified, trackHeight: Dp = Dp.Unspecified, segmentDotSize: Dp = Dp.Unspecified): SliderSpec
```
Creates a default  SliderSpec  object for sliders.