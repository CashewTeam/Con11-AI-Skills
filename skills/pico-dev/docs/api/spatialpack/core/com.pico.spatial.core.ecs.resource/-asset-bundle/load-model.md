# loadModel | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / loadModel 
# loadModel
```kotlin
fun loadModel(name: String): Entity
```
Loads a model by its name. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage it may cause jank or even ANR. 
- 
Prefer the async API  loadModelSuspend(...) . If you must use a sync call, execute it off the main thread or in a coroutine context such as  withContext(Dispatchers.IO) . 
#### Return
An  Entity  representing the root node of the loaded model. 
#### Parameters
name 
The name of the model to be loaded from the  AssetBundle . 
#### Throws
Illegal State Exception 
If the asset bundle is closed. 
Resource Loading Exception 
If any error occurs during the loading process.