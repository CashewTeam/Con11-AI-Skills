# setAmbientOcclusion | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicallyBasedMaterial / setAmbientOcclusion 
# setAmbientOcclusion
```kotlin
fun setAmbientOcclusion(ao: Float)
```
Sets the ambient occlusion value of the  PhysicallyBasedMaterial . 
The ambient occlusion property determines how much ambient light is occluded or blocked by the material. 
#### Parameters
ao 
The float value representing the ambient occlusion property of the material. Typically ranges from  0.0f  to  1.0f . The default value is  1.0f . A value of  0.0f  indicates no occlusion, meaning the surface is fully exposed to ambient light, while a value of  1.0f  indicates full occlusion, meaning the surface is completely shaded from ambient light. Intermediate values can be used for partial occlusion. 
#### Throws
Illegal State Exception 
If this material is closed or invalid.