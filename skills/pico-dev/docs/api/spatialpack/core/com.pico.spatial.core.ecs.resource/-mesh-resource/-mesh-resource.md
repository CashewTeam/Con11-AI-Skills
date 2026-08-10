# MeshResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource / MeshResource 
# MeshResource
```kotlin
constructor(path: String, loadType: LoadType = LoadType.FROM_ASSETS)
```
Constructs a mesh resource via file path. 
#### Parameters
path 
The given path. 
load Type 
The loading type, which determines where to load the mesh resource from. The default value is  FROM_ASSETS . 
#### Throws
Resource Loading Exception 
If any error occurs during the loading process.