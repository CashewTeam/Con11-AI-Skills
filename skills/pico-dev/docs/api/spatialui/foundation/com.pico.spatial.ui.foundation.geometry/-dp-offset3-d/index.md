# DpOffset3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.geometry / DpOffset3D 
# DpOffset3D
```kotlin
@Immutable
```class  DpOffset3D ( val  x :  Dp ,  val  y :  Dp ,  val  z :  Dp ) 
Represent a 3D offset in  Dp . 
#### Return
A  DpOffset3D  with the given  x ,  y  and  z  values. 
Members Members & Extensions 
## Constructors
Dp Offset3D 
```kotlin
constructor(x: Dp, y: Dp, z: Dp)
```
## Types
Companion 
```kotlin
object Companion
```
Holds built-in  DpOffset3D s. 
## Properties
x 
```kotlin
val x: Dp
```
The x value. 
y 
```kotlin
val y: Dp
```
The y value. 
z 
```kotlin
val z: Dp
```
The z value. 
## Functions
copy 
```kotlin
fun copy(x: Dp = this.x, y: Dp = this.y, z: Dp = this.z): DpOffset3D
```equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to Int Offset3D 
```kotlin
fun DpOffset3D.toIntOffset3D(density: Density): IntOffset3D
```
Convert  DpOffset3D  to  IntOffset3D 
to Offset3D 
```kotlin
fun DpOffset3D.toOffset3D(density: Density): Offset3D
```
Convert  Offset3D  to  DpOffset3D 
to String 
```kotlin
open override fun toString(): String
```