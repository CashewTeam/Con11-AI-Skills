# setAmbientOcclusionTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setAmbientOcclusionTexture 
# setAmbientOcclusionTexture
```kotlin
fun setAmbientOcclusionTexture(texture: TextureResource)
```
Sets the ambient occlusion texture of the  PhysicallyBasedMaterial . 
Ambient occlusion is used to simulate the self-shadowing effect that occurs in crevices and corners, enhancing the perception of depth and detail in the material. 
#### Parameters
texture 
The  TextureResource  object representing the ambient occlusion texture. 
#### Throws
Illegal State Exception 
If this material or the texture is closed or invalid.