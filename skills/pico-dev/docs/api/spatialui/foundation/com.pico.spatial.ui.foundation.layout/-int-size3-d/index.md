# IntSize3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / IntSize3D 
# IntSize3D
```kotlin
@Stable
```class  IntSize3D ( val  width :  Int ,  val  height :  Int ,  val  depth :  Int ) 
The 3D size of a layout. 
Members 
## Constructors
Int Size3D 
```kotlin
constructor(width: Int, height: Int, depth: Int)
```
## Types
Companion 
```kotlin
object Companion
```
the companion of IntSize3D 
## Properties
depth 
```kotlin
val depth: Int
```
the depth of the layout in the 3D coordinates space. 
height 
```kotlin
val height: Int
```
the height of the layout in the 3D coordinates space. 
width 
```kotlin
val width: Int
```
the width of the layout in the 3D coordinates space. 
## Functions
copy 
```kotlin
fun copy(width: Int = this.width, height: Int = this.height, depth: Int = this.depth): IntSize3D
```
copy the size with new width, height and depth. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```