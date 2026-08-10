# Color3 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Color3 
# Color3
```kotlin
class Color3
```
Represents a gamma color with red, green, blue components. Component values are typically in the range 0, 1, though this is not strictly enforced. 
Members 
## Constructors
Color3 
```kotlin
constructor(red: Float, green: Float, blue: Float)
```
Constructs a new  Color3  instance with the specified red, green, blue. 
```kotlin
constructor(another: Color3)
```
The constructor to initialize from another  Color3  instance. 
```kotlin
constructor(vector3: Vector3)
```
The constructor to initialize from a  Vector3  instance. 
## Properties
blue 
```kotlin
val blue: Float
```
The blue component of the  Color3  instance. 
green 
```kotlin
val green: Float
```
The green component of the  Color3  instance. 
red 
```kotlin
val red: Float
```
The red component of the  Color3  instance. 
## Functions
div 
```kotlin
operator fun div(another: Color3): Color3
```
Divides the  Color3  instance by another  Color3  instance. 
```kotlin
operator fun div(scalar: Float): Color3
```
Divides the  Color3  instance by a scalar value. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```minus 
```kotlin
operator fun minus(another: Color3): Color3
```
Minus another  Color3  instance. 
plus 
```kotlin
operator fun plus(another: Color3): Color3
```
Plus another  Color3  instance. 
times 
```kotlin
operator fun times(another: Color3): Color3
```
Multiplies the  Color3  instance by another  Color3  instance. 
```kotlin
operator fun times(scalar: Float): Color3
```
Multiplies the  Color3  instance by a scalar value. 
to String 
```kotlin
open override fun toString(): String
```