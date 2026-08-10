# loadTextureResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / loadTextureResource 
# loadTextureResource
```kotlin
fun loadTextureResource(path: String): TextureResource
```
Loads a texture resource from the specified path. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage it may cause jank or even ANR. 
- 
Prefer invoking this from a background thread or within a coroutine context such as  withContext(Dispatchers.IO) . 
#### Return
Returns a  TextureResource  object representing the loaded texture. 
#### Parameters
path 
The path to the texture resource within the  AssetBundle . 
#### Throws
Illegal State Exception 
If the asset bundle is closed. 
Resource Loading Exception 
If any error occurs during the loading process.