# load | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / GaussianSplattingResource / Companion / load 
# load
```kotlin
@JvmStatic
```fun  load ( path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ) :  GaussianSplattingResource 
Loads a  GaussianSplattingResource  via file path. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage it may cause jank or even ANR. 
- 
Prefer invoking this from a background thread or within a coroutine context such as  withContext(Dispatchers.IO) . 
#### Return
The  GaussianSplattingResource  loaded. 
#### Parameters
path 
The given path. 
load Type 
The loading type, which determines where to load the resource from. The default value is  FROM_ASSETS . 
#### Throws
Resource Loading Exception 
If an error occurs during the loading process.