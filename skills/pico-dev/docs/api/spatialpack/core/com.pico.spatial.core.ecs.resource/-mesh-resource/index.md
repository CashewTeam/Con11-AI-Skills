# MeshResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshResource 
# MeshResource
```kotlin
class MeshResource : Resource
```
A high-level representation of a collection of vertices and edges that define a shape. All models imported into the engine are measured in meters. 
Members 
## Constructors
Mesh Resource 
```kotlin
constructor(path: String, loadType: LoadType = LoadType.FROM_ASSETS)
```
Constructs a mesh resource via file path. 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  MeshResource . 
## Functions
close 
```kotlin
open override fun close()
```
You need to manually release the resource to free the memory it occupies. 
get Blend Shape Names 
```kotlin
fun getBlendShapeNames(): Array<String>
```
Gets the names of all blend shapes in the mesh. 
get Bounding Box 
```kotlin
fun getBoundingBox(): BoundingBox
```
Gets the bounding box information of the model. 
get Skeleton 
```kotlin
fun getSkeleton(): Skeleton?
```
Gets the skeleton information. 
has Skeleton 
```kotlin
fun hasSkeleton(): Boolean
```
Returns whether this mesh has a skeleton (i.e., is a skinned mesh). 
replace With Mesh Model 
```kotlin
fun replaceWithMeshModel(model: MeshModel, bounds: BoundingBox? = null): Boolean
```
Replaces the geometry of this  MeshResource  with data from a  MeshModel .