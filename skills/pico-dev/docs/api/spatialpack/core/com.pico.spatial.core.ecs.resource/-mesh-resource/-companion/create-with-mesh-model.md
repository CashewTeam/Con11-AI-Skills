# createWithMeshModel | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource / Companion / createWithMeshModel 
# createWithMeshModel
```kotlin
@JvmStatic
```fun  createWithMeshModel ( model :  MeshModel ,  bounds :  BoundingBox ?  =  null ,  name :  String ) :  MeshResource 
Creates a new  MeshResource  from a  MeshModel . 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage it may cause jank or even ANR. 
- 
Prefer invoking this from a background thread or within a coroutine context such as  withContext(Dispatchers.IO) . 
#### Return
A new  MeshResource  instance. 
#### Parameters
model 
The mesh geometry data. 
bounds 
Optional bounds. 
name 
The name for the created  MeshResource . 
#### Throws
Resource Loading Exception 
If the runtime fails to create the mesh resource.