# setDepthTest | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / VideoMaterial / setDepthTest 
# setDepthTest
```kotlin
fun setDepthTest(depthTest: Boolean)
```
Enables or disables depth testing for the  VideoMaterial . 
When depth testing is enabled, the renderer will check the depth buffer to determine if the material should be rendered in front of or behind other objects. Disabling depth testing may result in the material always being rendered on top, regardless of its actual depth in the scene. 
#### Parameters
depth Test 
Whether to enable depth testing.  true : enable;  false : disable. 
#### Throws
Illegal State Exception 
If this material has been closed or is invalid.