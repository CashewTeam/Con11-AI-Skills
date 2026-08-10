# replaceWithMeshModel | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource / replaceWithMeshModel 
# replaceWithMeshModel
```kotlin
fun replaceWithMeshModel(model: MeshModel, bounds: BoundingBox? = null): Boolean
```
Replaces the geometry of this  MeshResource  with data from a  MeshModel . 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage it may cause jank or even ANR. 
- 
Prefer invoking this from a background thread or within a coroutine context such as  withContext(Dispatchers.IO) . 
#### Return
true  if the replacement was applied;  false  otherwise. 
#### Parameters
model 
The mesh geometry data. 
bounds 
Optional bounds for the new geometry. 
#### Throws
Resource Loading Exception 
If the runtime fails to replace the mesh resource.