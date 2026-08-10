# Single | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ImageBasedLightSource / Single 
# Single
```kotlin
class Single(val resource: TextureResource) : ImageBasedLightSource
```
Provides local image-based lighting using a single environment texture. 
#### Parameters
resource 
The HDR environment  TextureResource  (typically a cubemap). Currently supported format:  .ktx . 
Members 
## Constructors
Single 
```kotlin
constructor(resource: TextureResource)
```
## Properties
resource 
```kotlin
val resource: TextureResource
```
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```