# Matrix4 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 
# Matrix4
```kotlin
class Matrix4(val m00: Float, val m01: Float, val m02: Float, val m03: Float, val m10: Float, val m11: Float, val m12: Float, val m13: Float, val m20: Float, val m21: Float, val m22: Float, val m23: Float, val m30: Float, val m31: Float, val m32: Float, val m33: Float)
```
Represents a 4x4 matrix. 
The  Matrix4  is implemented in row-major order and follows basic calculation principles: 
- 
Associativity: (m1 * m2) * m3 = m1 * (m2 * m3). 
- 
Distributivity: (m1 + m2) * m3 = (m1 * m3) + (m2 * m3). 
Members 
## Constructors
Matrix4 
```kotlin
constructor(m00: Float, m01: Float, m02: Float, m03: Float, m10: Float, m11: Float, m12: Float, m13: Float, m20: Float, m21: Float, m22: Float, m23: Float, m30: Float, m31: Float, m32: Float, m33: Float)
```
```kotlin
constructor(another: Matrix4)
```
Creates a new  Matrix4  based on another  Matrix4 . 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  Matrix4 . 
## Properties
forward 
```kotlin
val forward: Vector3
```
Gets the basis vector representing the Z-axis of the coordinate system after this matrix's transformation. This is commonly referred to as the "forward" vector. 
m00 
```kotlin
val m00: Float
```
The item locates in row index 0 and column index 0. 
m01 
```kotlin
val m01: Float
```
The item locates in row index 0 and column index 1. 
m02 
```kotlin
val m02: Float
```
The item locates in row index 0 and column index 2. 
m03 
```kotlin
val m03: Float
```
The item locates in row index 0 and column index 3. 
m10 
```kotlin
val m10: Float
```
The item locates in row index 1 and column index 0. 
m11 
```kotlin
val m11: Float
```
The item locates in row index 1 and column index 1. 
m12 
```kotlin
val m12: Float
```
The item locates in row index 1 and column index 2. 
m13 
```kotlin
val m13: Float
```
The item locates in row index 1 and column index 3. 
m20 
```kotlin
val m20: Float
```
The item locates in row index 2 and column index 0. 
m21 
```kotlin
val m21: Float
```
The item locates in row index 2 and column index 1. 
m22 
```kotlin
val m22: Float
```
The item locates in row index 2 and column index 2. 
m23 
```kotlin
val m23: Float
```
The item locates in row index 2 and column index 3. 
m30 
```kotlin
val m30: Float
```
The item locates in row index 3 and column index 0. 
m31 
```kotlin
val m31: Float
```
The item locates in row index 3 and column index 1. 
m32 
```kotlin
val m32: Float
```
The item locates in row index 3 and column index 2. 
m33 
```kotlin
val m33: Float
```
The item locates in row index 3 and column index 3. 
position 
```kotlin
val position: Vector3
```
Gets the position or translation component of this 4x4 matrix. 
right 
```kotlin
val right: Vector3
```
Gets the basis vector representing the X-axis of the coordinate system after this matrix's transformation. This is commonly referred to as the "right" vector. 
rotation 
```kotlin
val rotation: Quat
```
Extracts the pure rotational component of this 4x4 matrix as a  Quat  (quaternion). 
scale 
```kotlin
val scale: Vector3
```
Gets the apparent scaling factors along the local X, Y, and Z axes of the transformation represented by this matrix. 
translation 
```kotlin
val translation: Vector3
```
Gets the position or translation component of this 4x4 affine transformation matrix. 
up 
```kotlin
val up: Vector3
```
Gets the basis vector representing the Y-axis of the coordinate system after this matrix's transformation. This is commonly referred to as the "up" vector. 
## Functions
dec 
```kotlin
operator fun dec(): Matrix4
```
Overloads the unary decrement operator ( -- ). 
determinant 
```kotlin
fun determinant(): Float
```
Calculates the determinant of this 4x4 matrix. 
div 
```kotlin
operator fun div(scale: Float): Matrix4
```
Overloads the  /  operator to perform element-wise division of this matrix by a scalar value. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get 
```kotlin
operator fun get(row: Int, col: Int): Float
```
Gets the item with the row and column index from the  Matrix4  instance. 
hash Code 
```kotlin
open override fun hashCode(): Int
```inc 
```kotlin
operator fun inc(): Matrix4
```
Overloads the unary increment operator ( ++ ). 
inverse 
```kotlin
fun inverse(): Matrix4
```
Calculates and returns the inverse of this 4x4 matrix. 
is Finite 
```kotlin
fun isFinite(): Boolean
```
Checks if the value of the  Matrix4  instance is finite. 
minus 
```kotlin
operator fun minus(other: Matrix4): Matrix4
```
Overloads the  -  operator to perform element-wise subtraction of this matrix with another  Matrix4 . 
plus 
```kotlin
operator fun plus(other: Matrix4): Matrix4
```
Overloads the  +  operator to perform element-wise addition of this matrix with another  Matrix4 . 
times 
```kotlin
operator fun times(other: Matrix4): Matrix4
```
Times two  Matrix4  instances. 
```kotlin
operator fun times(other: Vector4): Vector4
```
Overloads the  *  operator to transform a 4D vector by this matrix. 
```kotlin
operator fun times(scale: Float): Matrix4
```
Overloads the  *  operator to perform element-wise multiplication of this matrix by a scalar value. 
to Float Array 
```kotlin
fun toFloatArray(): FloatArray
```
Converts the  Matrix4  instance to a float array. 
to String 
```kotlin
open override fun toString(): String
```to Transform 
```kotlin
fun toTransform(): Transform
```
Converts the  Matrix4  instance to a  Transform  object. 
transpose 
```kotlin
fun transpose(): Matrix4
```
Gets the transpose of this  Matrix4  instance. 
unary Minus 
```kotlin
operator fun unaryMinus(): Matrix4
```
Negates matrix data.