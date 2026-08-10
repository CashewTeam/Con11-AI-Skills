# setDepthWrite | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / VideoMaterial / setDepthWrite 
# setDepthWrite
```kotlin
fun setDepthWrite(depthWrite: Boolean)
```
Enables or disables depth writing for the  VideoMaterial . 
When depth writing is enabled, the material will update the depth buffer with its depth values. 
#### Parameters
depth Write 
Whether to enable depth writing.  true : enable;  false : disable. 
#### Throws
Illegal State Exception 
If this material has been closed or is invalid.