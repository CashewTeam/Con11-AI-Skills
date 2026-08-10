# load | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / Companion / load 
# load
```kotlin
@JvmStatic
```fun  load ( path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ) :  AssetBundle 
Loads an  AssetBundle  from a specified path. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage it may cause jank or even ANR. 
- 
Prefer invoking this from a background thread or within a coroutine context such as  withContext(Dispatchers.IO) . 
This static method supports loading  AssetBundle s from different sources. This flexibility facilitates the loading of  AssetBundle s in various environments and scenarios. 
#### Return
Returns an instance of the  AssetBundle  loaded from the specified path and load type. 
#### Parameters
path 
The path where the  AssetBundle  is located. 
load Type 
The type of loading operation, specifying where to load the  AssetBundle  from. Defaults to  FROM_ASSETS . 
#### Throws
Resource Loading Exception 
If any error occurs during the loading process.