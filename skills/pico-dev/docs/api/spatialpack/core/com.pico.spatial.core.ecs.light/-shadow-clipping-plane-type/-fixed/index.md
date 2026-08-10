# Fixed | PICO Spatial SDK

core / com.pico.spatial.core.ecs.light / ShadowClippingPlaneType / Fixed 
# Fixed
```kotlin
class Fixed(val zNear: Float = 0.01f, val zFar: Float = 10.0f) : ShadowClippingPlaneType
```
Uses fixed clipping planes for shadow rendering. 
Shadow clipping is defined by two planes orthogonal to the light direction, located at  zNear  and  zFar . 
Members 
## Constructors
Fixed 
```kotlin
constructor(zNear: Float = 0.01f, zFar: Float = 10.0f)
```
## Properties
z Far 
```kotlin
val zFar: Float
```
The distance to the far clipping plane. 
z Near 
```kotlin
val zNear: Float
```
The distance to the near clipping plane. 
## Functions
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