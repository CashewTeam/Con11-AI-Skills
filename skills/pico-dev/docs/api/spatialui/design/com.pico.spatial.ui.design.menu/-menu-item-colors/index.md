# MenuItemColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.menu / MenuItemColors 
# MenuItemColors
```kotlin
@Stable
```class  MenuItemColors 
Represents the container and content colors used in a list item in different states. 
- 
See DefaultColor for the default colors used in a  MenuItem . 
Members 
## Properties
container Color 
```kotlin
val containerColor: Color
```
for background shape color 
subtitle Color 
```kotlin
val subtitleColor: Color
```
subtitle content color, usually is for text color 
title Color 
```kotlin
val titleColor: Color
```
title content color, usually is for text color 
## Functions
copy 
```kotlin
fun copy(containerColor: Color = this.containerColor, titleColor: Color = this.titleColor, subtitleColor: Color = this.subtitleColor): MenuItemColors
```
copy a new instance 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```