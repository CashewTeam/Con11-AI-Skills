# loadFromAssetBundle | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / ShaderGraphMaterial / Companion / loadFromAssetBundle 
# loadFromAssetBundle
```kotlin
@JvmStatic
```fun  loadFromAssetBundle ( assetBundle :  AssetBundle ,  path :  String ) :  ShaderGraphMaterial 
Loads a  ShaderGraphMaterial  from  AssetBundle  through a relative path. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage it may cause jank or even ANR. 
- 
Prefer invoking this from a background thread or within a coroutine context such as  withContext(Dispatchers.IO) . 
#### Return
The  ShaderGraphMaterial  loaded. 
#### Parameters
asset Bundle 
The  AssetBundle  to load the  ShaderGraphMaterial  from. 
path 
The relative path. 
#### Throws
Illegal State Exception 
If the  AssetBundle  is closed. 
Resource Loading Exception 
If the loading fails.