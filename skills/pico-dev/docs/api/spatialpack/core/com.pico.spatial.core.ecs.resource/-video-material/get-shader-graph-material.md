# getShaderGraphMaterial | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / VideoMaterial / getShaderGraphMaterial 
# getShaderGraphMaterial
```kotlin
fun getShaderGraphMaterial(): ShaderGraphMaterial?
```
Gets the attached  ShaderGraphMaterial  of the VideoMaterial. 
#### Return
The  ShaderGraphMaterial  that VideoMaterial is using, or null if no  ShaderGraphMaterial  is attached. 
#### Throws
Illegal State Exception 
If this material has been closed or is invalid.