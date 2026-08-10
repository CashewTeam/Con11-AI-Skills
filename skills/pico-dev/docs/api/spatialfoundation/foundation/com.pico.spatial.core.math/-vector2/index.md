# Vector2 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 
# Vector2
```kotlin
class Vector2
```
Represents a vector2. 
Members 
## Constructors
Vector2 
```kotlin
constructor(x: Float, y: Float)
```
Creates a new  Vector2  instance with the specified x, y components. 
```kotlin
constructor(value: Float)
```
Initializes a  Vector2  instance with a single float value. 
```kotlin
constructor(other: Vector2)
```
Initializes a  Vector2  instance from another  Vector2  instance. 
```kotlin
constructor(other: Vector3)
```
Initializes a  Vector2  instance from a  Vector3  instance's x and y. 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  Vector2 . 
## Properties
x 
```kotlin
val x: Float
```
The x position of the  Vector2 . 
y 
```kotlin
val y: Float
```
The x position of the  Vector2 . 
## Functions
dec 
```kotlin
operator fun dec(): Vector2
```
Overloads the unary decrement operator ( -- ). 
div 
```kotlin
operator fun div(other: Vector2): Vector2
```
Divides this  Vector2  instance by another  Vector2  instance. 
```kotlin
operator fun div(scalar: Float): Vector2
```
Divides this  Vector2  instance by a scalar. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```inc 
```kotlin
operator fun inc(): Vector2
```
Overloads the unary increment operator ( ++ ). 
is Finite 
```kotlin
fun isFinite(): Boolean
```
Checks if the value of the  Vector2  instance is finite. 
length 
```kotlin
fun length(): Float
```
Gets the length of the  Vector2  instance. 
minus 
```kotlin
operator fun minus(other: Vector2): Vector2
```
Subtracts another  Vector2  instance from this  Vector2  instance. 
normalize 
```kotlin
fun normalize(): Vector2
```
Normalizes the  Vector2  instance. 
plus 
```kotlin
operator fun plus(other: Vector2): Vector2
```
Adds another  Vector2  instance to this  Vector2  instance. 
times 
```kotlin
operator fun times(other: Vector2): Vector2
```
Multiplies this  Vector2  instance by another  Vector2  instance. 
```kotlin
operator fun times(scalar: Float): Vector2
```
Multiplies this  Vector2  instance by a scalar. 
to String 
```kotlin
open override fun toString(): String
```unary Minus 
```kotlin
operator fun unaryMinus(): Vector2
```
Returns the negation of this  Vector2  instance, changing (x, y) to (-x, -y).