# setEmissiveTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setEmissiveTexture 
# setEmissiveTexture
```kotlin
fun setEmissiveTexture(texture: TextureResource)
```
Sets the emissive texture of the  PhysicallyBasedMaterial . 
The emissive texture is used to make parts of the material appear as if they are emitting light. This is useful for creating effects such as glowing elements or self-illuminated surfaces. 
#### Parameters
texture 
The  TextureResource  object representing the emissive texture. 
#### Throws
Illegal State Exception 
If this material or the texture is closed or invalid.