# Vector4 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 
# Vector4
```kotlin
class Vector4
```
Represents a Vector4. 
Members 
## Constructors
Vector4 
```kotlin
constructor(x: Float, y: Float, z: Float, w: Float)
```
Constructs a new  Vector4  instance with the specified x, y, z, and w positions. 
```kotlin
constructor(value: Float)
```
```kotlin
constructor(other: Vector3, w: Float)
```
```kotlin
constructor(other: Vector4)
```
## Types
Companion 
```kotlin
object Companion
```
The companion object of  Vector4 . 
## Properties
w 
```kotlin
val w: Float
```
The w position of the  Vector4  instance. 
x 
```kotlin
val x: Float
```
The x position of the  Vector4  instance. 
y 
```kotlin
val y: Float
```
The y position of the  Vector4  instance. 
z 
```kotlin
val z: Float
```
The z position of the  Vector4  instance. 
## Functions
dec 
```kotlin
operator fun dec(): Vector4
```
Overloads the unary decrement operator ( -- ). 
div 
```kotlin
operator fun div(other: Vector4): Vector4
```
Divides this  Vector4  instance by another  Vector4  instance. 
```kotlin
operator fun div(scalar: Float): Vector4
```
Divides this  Vector4  instance by a scalar. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```inc 
```kotlin
operator fun inc(): Vector4
```
Overloads the unary increment operator ( ++ ). 
is Finite 
```kotlin
fun isFinite(): Boolean
```
Checks if the value of the  Vector4  instance is finite. 
length 
```kotlin
fun length(): Float
```
Gets the length of the  Vector4  instance. 
minus 
```kotlin
operator fun minus(other: Vector4): Vector4
```
Subtracts another  Vector4  instance from this  Vector4  instance. 
normalize 
```kotlin
fun normalize(): Vector4
```
Normalizes the  Vector4  instance. 
plus 
```kotlin
operator fun plus(other: Vector4): Vector4
```
Adds another  Vector4  instance to this  Vector4  instance. 
times 
```kotlin
operator fun times(other: Vector4): Vector4
```
Multiplies this  Vector4  instance by another  Vector4  instance. 
```kotlin
operator fun times(scalar: Float): Vector4
```
Multiplies this  Vector4  instance by a scalar. 
to String 
```kotlin
open override fun toString(): String
```to Vector3 
```kotlin
fun toVector3(): Vector3
```
Converts this 4D vector to a 3D vector by discarding the w-component. 
unary Minus 
```kotlin
operator fun unaryMinus(): Vector4
```
Overloads the unary minus operator ( - ).