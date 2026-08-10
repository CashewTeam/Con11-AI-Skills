# setBaseColorTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setBaseColorTexture 
# setBaseColorTexture
```kotlin
fun setBaseColorTexture(texture: TextureResource)
```
Sets the base color of the  PhysicallyBasedMaterial  using a texture. 
This method allows you to apply a texture to the material, which will be used as the base color. Textures can provide more complex and detailed color information compared to a single color value. 
#### Parameters
texture 
The  TextureResource  object representing the color texture to be applied to the material. 
#### Throws
Illegal State Exception 
If this material or the texture is closed or invalid.