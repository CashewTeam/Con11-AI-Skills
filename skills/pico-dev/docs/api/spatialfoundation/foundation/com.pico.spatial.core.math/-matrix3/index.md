# Matrix3 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix3 
# Matrix3
```kotlin
class Matrix3(val m00: Float, val m01: Float, val m02: Float, val m10: Float, val m11: Float, val m12: Float, val m20: Float, val m21: Float, val m22: Float)
```
Represents a 3x3 matrix. 
Note:  Matrix3  is implemented in row-major order. 
The  Matrix3  follows basic calculation principles: 
- 
Associativity: (m1 * m2) * m3 = m1 * (m2 * m3). 
- 
Distributivity: (m1 + m2) * m3 = (m1 * m3) + (m2 * m3). 
Members 
## Constructors
Matrix3 
```kotlin
constructor(m00: Float, m01: Float, m02: Float, m10: Float, m11: Float, m12: Float, m20: Float, m21: Float, m22: Float)
```
```kotlin
constructor(another: Matrix3)
```
Constructs to generate a new  Matrix3  based on another  Matrix3  instance. 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  Matrix3 . 
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
right 
```kotlin
val right: Vector3
```
Gets the basis vector representing the X-axis of the coordinate system after this matrix's transformation. This is commonly referred to as the "right" vector. 
up 
```kotlin
val up: Vector3
```
Gets the basis vector representing the Y-axis of the coordinate system after this matrix's transformation. This is commonly referred to as the "up" vector. 
## Functions
dec 
```kotlin
operator fun dec(): Matrix3
```
Overloads the unary decrement operator ( -- ). 
determinant 
```kotlin
fun determinant(): Float
```
Calculates the determinant of this 3x3 matrix. 
div 
```kotlin
operator fun div(scale: Float): Matrix3
```
Overloads the  /  operator to perform element-wise division of this matrix by a scalar value. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get 
```kotlin
operator fun get(row: Int, col: Int): Float
```
Gets the item with the row and column index from the  Matrix3  instance. 
hash Code 
```kotlin
open override fun hashCode(): Int
```inc 
```kotlin
operator fun inc(): Matrix3
```
Overloads the unary increment operator ( ++ ). 
inverse 
```kotlin
fun inverse(): Matrix3
```
Calculates the inverse of this 3x3 matrix. 
is Finite 
```kotlin
fun isFinite(): Boolean
```
Check if the  Matrix3  instance value is finite. 
minus 
```kotlin
operator fun minus(other: Matrix3): Matrix3
```
Overloads the  -  operator to perform element-wise subtraction of another  Matrix3  from this matrix. 
plus 
```kotlin
operator fun plus(other: Matrix3): Matrix3
```
Overloads the  +  operator to perform element-wise addition of this matrix with another  Matrix3 . 
times 
```kotlin
operator fun times(other: Matrix3): Matrix3
```
Overloads the  *  operator to perform matrix multiplication of this matrix by another  Matrix3  ( this * other ). 
```kotlin
operator fun times(other: Vector3): Vector3
```
Overloads the  *  operator to transform a 3D vector by this matrix. 
```kotlin
operator fun times(scale: Float): Matrix3
```
Overloads the  *  operator to perform element-wise multiplication of this matrix by a scalar value. 
to Float Array 
```kotlin
fun toFloatArray(): FloatArray
```
Converts the  Matrix3  to a float array. 
to String 
```kotlin
open override fun toString(): String
```transpose 
```kotlin
fun transpose(): Matrix3
```
Gets the transposed matrix of this matrix. 
unary Minus 
```kotlin
operator fun unaryMinus(): Matrix3
```
Overloads the unary minus operator ( - ) to perform element-wise negation of this matrix.