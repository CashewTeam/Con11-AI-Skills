# preloadModel | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / preloadModel 
# preloadModel
```kotlin
fun preloadModel(name: String)
```
Preloads the specified model into memory. 
Loading a model in advance ensures that it is immediately available when needed. This preloading operation reduces loading times and improves performance by preparing resources ahead of use. 
#### Parameters
name 
The name of the model to be preloaded. The name should correspond to the identifier used within the application to reference the model. 
Note: Ensure that the model name is valid and corresponds to an existing resource. This function assumes that the necessary resources are available and correctly configured.