# ListItemColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ListItemColors 
# ListItemColors
```kotlin
@Immutable
```class  ListItemColors 
Represents the container and content colors used in a list item in different states. 
Members 
## Properties
background Color 
```kotlin
val backgroundColor: Color
```
for background shape color 
headline Color 
```kotlin
val headlineColor: Color
```
headline content color, usually is for text color 
leading Color 
```kotlin
val leadingColor: Color
```
leading content color, such as icon & text color 
supporting Color 
```kotlin
val supportingColor: Color
```
supporting content color, usually is for text color 
trailing Color 
```kotlin
val trailingColor: Color
```
trailing content color, such as icon & text color 
## Functions
copy 
```kotlin
fun copy(backgroundColor: Color = this.backgroundColor, leadingColor: Color = this.leadingColor, headlineColor: Color = this.headlineColor, supportingColor: Color = this.supportingColor, trailingColor: Color = this.trailingColor): ListItemColors
```
copy a new instance 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```