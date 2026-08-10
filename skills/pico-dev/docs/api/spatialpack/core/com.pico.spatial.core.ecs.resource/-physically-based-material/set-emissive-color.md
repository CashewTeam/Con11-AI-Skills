# setEmissiveColor | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setEmissiveColor 
# setEmissiveColor
```kotlin
fun setEmissiveColor(color: Color4)
```
Sets the emissive color of the  PhysicallyBasedMaterial . 
The emissive color is used to make parts of the material appear as if they are emitting light. This is useful for creating effects such as glowing elements or self-illuminated surfaces. 
#### Parameters
color 
The  Color4  object representing the emissive color. The default value is  Color4(1f, 1f, 1f, 1f) . 
#### Throws
Illegal State Exception 
If this material is closed or invalid.