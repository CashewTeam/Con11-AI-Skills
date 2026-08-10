# BadgeColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / BadgeColors 
# BadgeColors
```kotlin
@Immutable
```class  BadgeColors ( val  backgroundColor :  Color ,  val  contentColor :  Color ) 
Color defs for badge 
Members 
## Constructors
Badge Colors 
```kotlin
constructor(backgroundColor: Color, contentColor: Color)
```
## Properties
background Color 
```kotlin
val backgroundColor: Color
```
backgroundColor 
content Color 
```kotlin
val contentColor: Color
```
content color, maybe text color or image tint color 
## Functions
copy 
```kotlin
@Stable
```fun  copy ( backgroundColor :  Color  =  this.backgroundColor ,  contentColor :  Color  =  this.contentColor ) :  BadgeColors 
Create a new  BadgeColors  instance with expected background color and content color. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```