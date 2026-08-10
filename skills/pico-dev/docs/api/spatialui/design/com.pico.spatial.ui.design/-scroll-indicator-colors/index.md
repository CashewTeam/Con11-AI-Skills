# ScrollIndicatorColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ScrollIndicatorColors 
# ScrollIndicatorColors
```kotlin
@Immutable
```class  ScrollIndicatorColors ( val  trackColor :  Color ,  val  indicatorColor :  Color ,  val  scrollMarksColor :  Color ,  val  backgroundColor :  Color ) 
Colors for  ScrollIndicator . 
#### Parameters
track Color 
The color of the track. 
indicator Color 
The color of the indicator. 
scroll Marks Color 
The color of the scrollingMarks. 
background Color 
The color of the background. 
Members 
## Constructors
Scroll Indicator Colors 
```kotlin
constructor(trackColor: Color, indicatorColor: Color, scrollMarksColor: Color, backgroundColor: Color)
```
## Properties
background Color 
```kotlin
val backgroundColor: Color
```indicator Color 
```kotlin
val indicatorColor: Color
```scroll Marks Color 
```kotlin
val scrollMarksColor: Color
```track Color 
```kotlin
val trackColor: Color
```
## Functions
copy 
```kotlin
@Stable
```fun  copy ( trackColor :  Color  =  this.trackColor ,  indicatorColor :  Color  =  this.indicatorColor ,  scrollMarksColor :  Color  =  this.scrollMarksColor ,  backgroundColor :  Color  =  this.backgroundColor ) :  ScrollIndicatorColors equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```