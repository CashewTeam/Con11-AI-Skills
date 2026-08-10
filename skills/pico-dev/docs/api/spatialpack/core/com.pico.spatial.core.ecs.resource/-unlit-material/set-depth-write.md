# setDepthWrite | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / UnlitMaterial / setDepthWrite 
# setDepthWrite
```kotlin
fun setDepthWrite(depthWrite: Boolean)
```
Enables or disables depth writing for the  UnlitMaterial . 
When depth writing is enabled, the material will update the depth buffer with its depth values. 
#### Parameters
depth Write 
Whether to enable depth writing.  true : enable;  false : disable. 
#### Throws
Illegal State Exception 
If this material is closed or invalid.