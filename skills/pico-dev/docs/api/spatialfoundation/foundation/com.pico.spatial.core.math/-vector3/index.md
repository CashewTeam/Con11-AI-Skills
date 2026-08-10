# Vector3 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 
# Vector3
```kotlin
class Vector3
```
Represents a vector3. 
Members 
## Constructors
Vector3 
```kotlin
constructor(x: Float = 0.0f, y: Float = 0.0f, z: Float = 0.0f)
```
Creates a new  Vector3  instance with the specified x, y, z positions. 
```kotlin
constructor(value: Float = 0.0f)
```
Initializes a  Vector3  instance with a single float value. 
```kotlin
constructor(other: Vector3)
```
Initializes a  Vector3  instance from another  Vector3  instance. 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  Vector3 . 
## Properties
x 
```kotlin
val x: Float
```
The x position of the  Vector3  instance. 
y 
```kotlin
val y: Float
```
The y position of the  Vector3  instance. 
z 
```kotlin
val z: Float
```
The z position of the  Vector3  instance. 
## Functions
dec 
```kotlin
operator fun dec(): Vector3
```
Overloads the decrement operator  --  to decrement each component of the current  Vector3  instance. 
div 
```kotlin
operator fun div(other: Vector3): Vector3
```
Divides this  Vector3  instance by another  Vector3  instance. 
```kotlin
operator fun div(scalar: Float): Vector3
```
Divides this  Vector3  instance by a scalar. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```inc 
```kotlin
operator fun inc(): Vector3
```
Overloads the unary increment operator ( ++ ). 
is Finite 
```kotlin
fun isFinite(): Boolean
```
Checks if the value of the  Vector3  instance is finite. 
length 
```kotlin
fun length(): Float
```
Gets the length of the  Vector3  instance. 
minus 
```kotlin
operator fun minus(other: Vector3): Vector3
```
Subtracts another  Vector3  instance from this  Vector3  instance. 
normalize 
```kotlin
fun normalize(): Vector3
```
Normalizes the  Vector3  instance. 
plus 
```kotlin
operator fun plus(other: Vector3): Vector3
```
Adds another  Vector3  instance to this  Vector3  instance. 
times 
```kotlin
operator fun times(other: Vector3): Vector3
```
Multiplies this  Vector3  instance by another  Vector3  instance. 
```kotlin
operator fun times(scalar: Float): Vector3
```
Multiplies this  Vector3  instance by a scalar. 
to Color4 
```kotlin
fun toColor4(alpha: Float): Color4
```
Converts this vector (interpreted as RGB color components) and a given alpha value into a Color4 object. 
to String 
```kotlin
open override fun toString(): String
```to Vector4 
```kotlin
fun toVector4(): Vector4
```
Converts this 3D vector into a 4D vector, treating it as a point in homogeneous coordinates. 
unary Minus 
```kotlin
operator fun unaryMinus(): Vector3
```
Overloads the unary minus operator ( - ).