# setRoughnessTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setRoughnessTexture 
# setRoughnessTexture
```kotlin
fun setRoughnessTexture(texture: TextureResource)
```
Sets the roughness of the  PhysicallyBasedMaterial  using a texture. 
This method allows for more detailed control over the roughness by using a texture, where different parts of the material can have varying roughness values. 
#### Parameters
texture 
The  TextureResource  object representing the roughness texture to be applied to the material. 
#### Throws
Illegal State Exception 
If this material or the texture is closed or invalid.