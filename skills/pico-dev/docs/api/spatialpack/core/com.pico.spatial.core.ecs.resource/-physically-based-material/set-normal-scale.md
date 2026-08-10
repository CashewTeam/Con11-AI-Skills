# setNormalScale | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setNormalScale 
# setNormalScale
```kotlin
fun setNormalScale(scale: Float)
```
Sets the normal scale of the  PhysicallyBasedMaterial . 
The normal scale is used to adjust the strength of the normal map effect. 
#### Parameters
scale 
The float value representing the normal scale of the material, which ranges from  0.0f  (no normal map) to  1.0f  (full strength). The default value is  1.0f . A higher value will increase the strength of the normal map, while a lower value will reduce it. 
#### Throws
Illegal State Exception 
If this material is closed or invalid.