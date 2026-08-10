# setNormalTexture | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setNormalTexture 
# setNormalTexture
```kotlin
fun setNormalTexture(texture: TextureResource)
```
Sets the normal texture of the  PhysicallyBasedMaterial . 
The normal texture, or normal map, is used to simulate fine surface details and bumps without increasing the polygon count. It alters the surface normals to create the illusion of complex surface geometry. 
#### Parameters
texture 
The  TextureResource  object representing the normal texture. 
#### Throws
Illegal State Exception 
If this material or the texture is closed or invalid.