# setMetallic | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setMetallic 
# setMetallic
```kotlin
fun setMetallic(metallic: Float)
```
Sets the metallic value of the  PhysicallyBasedMaterial . 
The metallic value determines how metallic the surface appears. 
#### Parameters
metallic 
The float value representing the metallic property of the material, which ranges from  0.0f  to  1.0f . The default value is  1.0f . A value of  0.0f  indicates a non-metallic surface, while a value of  1.0f  indicates a fully metallic surface. Intermediate values can be used for partially metallic surfaces. 
#### Throws
Illegal State Exception 
If this material is closed or invalid.