# loadModelSuspend | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / loadModelSuspend 
# loadModelSuspend
```kotlin
suspend fun loadModelSuspend(name: String): Entity
```
Asynchronously loads a model by its name. This is a suspend function. 
#### Return
An  Entity  representing the root node of the loaded model scene. 
#### Parameters
name 
The name of the model to be loaded from the AssetBundle. 
#### Throws
Illegal State Exception 
If the asset bundle is closed. 
Resource Loading Exception 
If any error occurs during the loading process.