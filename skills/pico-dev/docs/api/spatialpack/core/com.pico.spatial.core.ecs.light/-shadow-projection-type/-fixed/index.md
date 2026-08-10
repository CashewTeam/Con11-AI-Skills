# Fixed | PICO Spatial SDK

core / com.pico.spatial.core.ecs.light / ShadowProjectionType / Fixed 
# Fixed
```kotlin
class Fixed(val zNear: Float = 0.01f, val zFar: Float = 10.0f, val orthographicWidth: Float = 10.0f, val orthographicHeight: Float = 10.0f) : ShadowProjectionType
```
Uses fixed parameters to define the shadow projection. 
The projection frustum is bounded by two planes orthogonal to the light direction at  zNear  and  zFar , and by the orthographic extents defined by  orthographicWidth  and  orthographicHeight . 
Members 
## Constructors
Fixed 
```kotlin
constructor(zNear: Float = 0.01f, zFar: Float = 10.0f, orthographicWidth: Float = 10.0f, orthographicHeight: Float = 10.0f)
```
## Properties
orthographic Height 
```kotlin
val orthographicHeight: Float
```
The height of the orthographic shadow projection. 
orthographic Width 
```kotlin
val orthographicWidth: Float
```
The width of the orthographic shadow projection. 
z Far 
```kotlin
val zFar: Float
```
The distance to the far plane of the shadow projection frustum. 
z Near 
```kotlin
val zNear: Float
```
The distance to the near plane of the shadow projection frustum. 
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