# ChipColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ChipColors 
# ChipColors
```kotlin
@Immutable
```open  class  ChipColors 
colors for  Chip 
#### Inheritors
ToggleableChipColors Members 
## Properties
background Color 
```kotlin
val backgroundColor: Color
```
background color 
content Color 
```kotlin
val contentColor: Color
```
Color for label and icon 
## Functions
copy 
```kotlin
fun copy(contentColor: Color = this.contentColor, backgroundColor: Color = this.backgroundColor): ChipColors
```
Create a new  ChipColors  instance with expected background color and content color. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```