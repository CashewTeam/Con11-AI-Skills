# setRoughness | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setRoughness 
# setRoughness
```kotlin
fun setRoughness(roughness: Float)
```
Sets the roughness value of the  PhysicallyBasedMaterial . 
Roughness controls how smooth or rough the surface appears. 
#### Parameters
roughness 
The float value representing the roughness of the material, which ranges from  0.0f  to  1.0f . The default value is  1.0f . A lower roughness value results in a smoother surface, while a higher roughness value makes the surface appear rougher. 
#### Throws
Illegal State Exception 
If this material is closed or invalid.