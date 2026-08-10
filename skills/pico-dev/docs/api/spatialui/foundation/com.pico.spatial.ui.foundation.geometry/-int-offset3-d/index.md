# IntOffset3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.geometry / IntOffset3D 
# IntOffset3D
```kotlin
@Immutable
```class  IntOffset3D ( val  x :  Int ,  val  y :  Int ,  val  z :  Int ) 
Represent a 3D offset in pixel. 
#### Return
A  IntOffset3D  with the given  x ,  y  and  z  values. 
#### Parameters
x 
The x value. 
y 
The y value. 
z 
The z value. 
Members 
## Constructors
Int Offset3D 
```kotlin
constructor(x: Int, y: Int, z: Int)
```
## Types
Companion 
```kotlin
object Companion
```
Holds built-in  IntOffset3D s. 
## Properties
x 
```kotlin
val x: Int
```y 
```kotlin
val y: Int
```z 
```kotlin
val z: Int
```
## Functions
copy 
```kotlin
fun copy(x: Int = this.x, y: Int = this.y, z: Int = this.z): IntOffset3D
```equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```