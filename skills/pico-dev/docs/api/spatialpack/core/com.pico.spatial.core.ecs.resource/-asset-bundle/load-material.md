# loadMaterial | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / loadMaterial 
# loadMaterial
```kotlin
fun loadMaterial(path: String): Material
```
Loads a material from the specified path. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage it may cause jank or even ANR. 
- 
Prefer invoking this from a background thread or within a coroutine context such as  withContext(Dispatchers.IO) . 
#### Return
Returns a  Material  object representing the loaded material. 
#### Parameters
path 
The path to the material to be loaded in the  AssetBundle . 
#### Throws
Resource Loading Exception 
If any error occurs during the loading process.