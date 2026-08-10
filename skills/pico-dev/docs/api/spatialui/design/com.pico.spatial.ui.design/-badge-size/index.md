# BadgeSize | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / BadgeSize 
# BadgeSize
```kotlin
@Stable
```class  BadgeSize 
BadgeSize 
Members Members & Extensions 
## Properties
height 
```kotlin
val height: Dp
```
badge height 
width 
```kotlin
val width: Dp
```
badge width 
## Functions
badge Padding 
```kotlin
@Composable
```fun  BadgeSize . badgePadding ( ) :  PaddingValues 
Calculates the inner padding values for a badge based on its size. 
badge Radius 
```kotlin
fun BadgeSize.badgeRadius(): Dp
```
Calculates the corner radius for a badge. This function determines the appropriate radius based on the badge size. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```