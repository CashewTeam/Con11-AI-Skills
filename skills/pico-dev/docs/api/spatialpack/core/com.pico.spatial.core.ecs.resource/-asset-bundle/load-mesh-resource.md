# loadMeshResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / loadMeshResource 
# loadMeshResource
```kotlin
fun loadMeshResource(path: String): MeshResource
```
Loads a mesh resource from the specified path. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage it may cause jank or even ANR. 
- 
Prefer invoking this from a background thread or within a coroutine context such as  withContext(Dispatchers.IO) . 
#### Return
Returns a  MeshResource  object representing the loaded mesh. 
#### Parameters
path 
The path to the mesh resource within the  AssetBundle . 
#### Throws
Illegal State Exception 
If the asset bundle is closed. 
Resource Loading Exception 
If any error occurs during the loading process.