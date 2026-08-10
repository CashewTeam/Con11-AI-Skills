# ToggleableChipColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ToggleableChipColors 
# ToggleableChipColors
```kotlin
@Immutable
```class  ToggleableChipColors  :  ChipColors 
colors for  ToggleableChip 
#### Parameters
content Color 
The content color of the chip. 
background Color 
The background color of the chip. 
Members 
## Properties
active Background Color 
```kotlin
val activeBackgroundColor: Color
```
background color when toggle state is on 
active Content Color 
```kotlin
val activeContentColor: Color
```
content color when toggle state is on 
## Functions
copy 
```kotlin
fun copy(contentColor: Color = this.contentColor, backgroundColor: Color = this.backgroundColor, activeContentColor: Color = this.activeContentColor, activeBackgroundColor: Color = this.activeBackgroundColor): ToggleableChipColors
```
Create a new  ToggleableChipColors  instance with the specified color properties. If some color values are not provided, the color values of the current instance are used. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```