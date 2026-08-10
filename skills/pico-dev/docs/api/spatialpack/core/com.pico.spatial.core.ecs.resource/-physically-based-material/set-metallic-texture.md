# setMetallicTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setMetallicTexture 
# setMetallicTexture
```kotlin
fun setMetallicTexture(texture: TextureResource)
```
Sets the metallic property of the  PhysicallyBasedMaterial  using a texture. 
This method allows for more nuanced control over the metallic property by using a texture, where different parts of the material can have varying metallic values. 
#### Parameters
texture 
The  TextureResource  object representing the metallic texture to be applied to the material. 
#### Throws
Illegal State Exception 
If this material or the texture is closed or invalid.