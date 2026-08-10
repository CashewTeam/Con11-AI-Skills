# getParameterNames | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ShaderGraphMaterial / getParameterNames 
# getParameterNames
```kotlin
fun getParameterNames(): Array<String>
```
Gets all parameter names of the  ShaderGraphMaterial . 
#### Return
The array of all parameter names. 
#### Throws
Illegal State Exception 
If this material is closed or invalid. 
Resource Loading Exception 
If any error occurs when retrieving the parameter names.