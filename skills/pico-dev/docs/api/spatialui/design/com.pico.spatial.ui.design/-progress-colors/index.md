# ProgressColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ProgressColors 
# ProgressColors
```kotlin
@Immutable
```open  class  ProgressColors 
defines colors for progress indicator 
Members 
## Properties
background Color 
```kotlin
val backgroundColor: Color
```
background color 
indicator Color 
```kotlin
val indicatorColor: Color
```
progress bar color 
## Functions
copy 
```kotlin
fun copy(indicatorColor: Color = this.indicatorColor, backgroundColor: Color = this.backgroundColor): ProgressColors
```equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```