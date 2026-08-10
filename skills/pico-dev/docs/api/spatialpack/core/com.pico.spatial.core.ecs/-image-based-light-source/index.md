# ImageBasedLightSource | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ImageBasedLightSource 
# ImageBasedLightSource
```kotlin
sealed class ImageBasedLightSource
```
Defines the source textures for image-based lighting (IBL) in a scene. 
This sealed class hierarchy represents different configurations for environment lighting sources, supporting both single textures and blended combinations. Used with  ImageBasedLightComponent  to provide realistic environment lighting. 
### Source Types:
- 
None  - Disables local image-based lighting. 
- 
Single  - Uses a single environment texture. 
- 
Blend  - Combines two environment textures with controllable blending. 
#### Inheritors
None Single Blend Members 
## Constructors
Image Based Light Source 
```kotlin
protected constructor()
```
## Types
Blend 
```kotlin
class Blend(val firstResource: TextureResource, val secondResource: TextureResource, val blendPercentage: Float = 0.5f) : ImageBasedLightSource
```
Provides blended image-based lighting from two environment textures. 
None 
```kotlin
object None : ImageBasedLightSource
```
Disables local image-based lighting for the associated component. 
Single 
```kotlin
class Single(val resource: TextureResource) : ImageBasedLightSource
```
Provides local image-based lighting using a single environment texture.