# load | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource / Companion / load 
# load
```kotlin
@JvmStatic
```fun  load ( path :  String ,  loadType :  LoadType  =  LoadType.FROM_ASSETS ) :  MeshResource 
Loads a  MeshResource  via file path. 
#### Return
The  MeshResource  loaded. 
#### Parameters
path 
The given path. 
load Type 
The loading type, which determines where to load the mesh resource from. The default value is  FROM_ASSETS . 
#### Throws
Resource Loading Exception 
If an error occurs during the loading process. 
Note: For complex or high-resolution resources that require significant processing time, it is strongly recommended to leverage coroutines for loading. This approach prevents blocking the main thread, ensuring a responsive and fluid user experience.