# Blend | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ImageBasedLightSource / Blend 
# Blend
```kotlin
class Blend(val firstResource: TextureResource, val secondResource: TextureResource, val blendPercentage: Float = 0.5f) : ImageBasedLightSource
```
Provides blended image-based lighting from two environment textures. 
#### Parameters
first Resource 
The primary environment texture. 
second Resource 
The secondary environment texture to blend with. 
blend Percentage 
The blend ratio, where  0.0  = 100% first texture,  1.0  = 100% second texture. The default value is  0.5  (equal blend). 
Members 
## Constructors
Blend 
```kotlin
constructor(firstResource: TextureResource, secondResource: TextureResource, blendPercentage: Float = 0.5f)
```
## Properties
blend Percentage 
```kotlin
val blendPercentage: Float
```first Resource 
```kotlin
val firstResource: TextureResource
```second Resource 
```kotlin
val secondResource: TextureResource
```
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```