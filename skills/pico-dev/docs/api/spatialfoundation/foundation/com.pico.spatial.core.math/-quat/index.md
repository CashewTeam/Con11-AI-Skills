# Quat | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat 
# Quat
```kotlin
class Quat
```
Represents a quaternion. 
Members 
## Constructors
Quat 
```kotlin
constructor(x: Float, y: Float, z: Float, w: Float)
```
Constructs a new  Quat  instance with the specified x, y, z, and w components. 
```kotlin
constructor()
```
The default  Quat  constructor. 
```kotlin
constructor(another: Quat)
```
Initializes a new  Quat  instance from another existing  Quat  instance. 
```kotlin
constructor(rotAxis: Vector3, rotAngle: Float)
```
Initializes a  Quat  instance using an angle and axis of rotation. 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  Quat . 
## Properties
w 
```kotlin
val w: Float
```
The w position of the  Quat . 
x 
```kotlin
val x: Float
```
The x position of the  Quat . 
y 
```kotlin
val y: Float
```
The y position of the  Quat . 
z 
```kotlin
val z: Float
```
The z position of the  Quat . 
## Functions
conjugate 
```kotlin
fun conjugate(): Quat
```
Calculates and returns the conjugate of this quaternion. 
div 
```kotlin
operator fun div(scalar: Float): Quat
```
Overloads the  /  operator to perform element-wise division of this quaternion by a scalar value. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```equivalent Check 
```kotlin
fun equivalentCheck(other: Quat): Boolean
```
Determine whether two rotation operations are equivalent. 
hash Code 
```kotlin
open override fun hashCode(): Int
```is Finite 
```kotlin
fun isFinite(): Boolean
```
Check if the Quat instance value is finite. 
length 
```kotlin
fun length(): Float
```
Calculates the length (magnitude or norm) of this quaternion. 
minus 
```kotlin
operator fun minus(other: Quat): Quat
```
Overloads the  -  operator to perform component-wise subtraction of another quaternion ( other ) from this quaternion ( this ). 
normalize 
```kotlin
fun normalize(): Quat
```
Returns a new quaternion with the same direction as this quaternion but with a length (magnitude) of 1.0. 
plus 
```kotlin
operator fun plus(other: Quat): Quat
```
Overloads the  +  operator to perform component-wise addition of this quaternion with another quaternion. 
rotate Vector 
```kotlin
fun rotateVector(vector: Vector3): Vector3
```
Rotates the given Vector3 by this quaternion. 
times 
```kotlin
operator fun times(other: Quat): Quat
```
Times two  Quat  instances. 
```kotlin
operator fun times(scalar: Float): Quat
```
Overloads the  *  operator to perform multiplication of this quaternion by a scalar value. 
to Angle Axis 
```kotlin
fun toAngleAxis(): Pair<Float, Vector3>
```
Converts this quaternion to its equivalent angle-axis representation, with the angle returned in  degrees . 
to Euler Angles 
```kotlin
fun toEulerAngles(): EulerAngles
```
Converts the  Quat  instance to the  EulerAngles  instance. 
to Matrix 
```kotlin
fun toMatrix(): Matrix4
```
Converts this quaternion into an equivalent 4x4 rotation matrix. 
to String 
```kotlin
open override fun toString(): String
```unary Minus 
```kotlin
operator fun unaryMinus(): Quat
```
Overloads the unary minus operator ( - ) to perform component-wise negation of this quaternion.