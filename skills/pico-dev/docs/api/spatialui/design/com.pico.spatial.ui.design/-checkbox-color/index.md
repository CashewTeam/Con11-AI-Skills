# CheckboxColor | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / CheckboxColor 
# CheckboxColor
```kotlin
@Immutable
```class  CheckboxColor 
colors wrapper for  Checkbox 
Members 
## Properties
background Color 
```kotlin
val backgroundColor: Color
```
background color of the content, e.g. circle 
border Color 
```kotlin
val borderColor: Color
```
unchecked border color 
content Color 
```kotlin
val contentColor: Color
```
content color, e.g. tick 
## Functions
copy 
```kotlin
@Stable
```fun  copy ( backgroundColor :  Color  =  this.backgroundColor ,  contentColor :  Color  =  this.contentColor ,  borderColor :  Color  =  this.borderColor ) :  CheckboxColor 
Creates a new  CheckboxColor  instance. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```