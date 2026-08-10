# detachShaderGraphMaterial | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / VideoMaterial / detachShaderGraphMaterial 
# detachShaderGraphMaterial
```kotlin
fun detachShaderGraphMaterial()
```
Detaches the previously attached ShaderGraphMaterial from the VideoMaterial. 
Note: After detachment, the ShaderGraphMaterial will no longer be used by the VideoMaterial and will be released automatically. To avoid it being released by this method,  .toGlobal()  should be called on the ShaderGraphMaterial instance before calling  detachShaderGraphMaterial  if reuse is intended, please see  attachShaderGraphMaterial  use example. 
#### Throws
Illegal State Exception 
If this material has been closed or is invalid.