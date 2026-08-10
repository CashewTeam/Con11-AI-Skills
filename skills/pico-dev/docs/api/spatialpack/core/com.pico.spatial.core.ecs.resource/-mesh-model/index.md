# MeshModel | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshModel 
# MeshModel
```kotlin
class MeshModel @JvmOverloads constructor(val positions: List<Vector3>, val triangleIndices: List<Int>, val normals: List<Vector3>? = null, val tangents: List<Vector4>? = null, val uv0: List<Vector2>? = null, val uv1: List<Vector2>? = null, val colors: List<Color4>? = null)
```
A container for mesh geometry data. 
The fields describe the vertex attributes and triangle indices used to build a mesh. 
Members 
## Constructors
Mesh Model 
```kotlin
@JvmOverloads
```constructor ( positions :  List < Vector3 > ,  triangleIndices :  List < Int > ,  normals :  List < Vector3 > ?  =  null ,  tangents :  List < Vector4 > ?  =  null ,  uv0 :  List < Vector2 > ?  =  null ,  uv1 :  List < Vector2 > ?  =  null ,  colors :  List < Color4 > ?  =  null ) 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  MeshModel . 
## Properties
colors 
```kotlin
val colors: List<Color4>?
```
Per-vertex colors in linear space. Optional. 
normals 
```kotlin
val normals: List<Vector3>?
```
Per-vertex normals. Optional. 
positions 
```kotlin
val positions: List<Vector3>
```
The vertex positions of the mesh. 
tangents 
```kotlin
val tangents: List<Vector4>?
```
Per-vertex tangents. Optional. 
triangle Indices 
```kotlin
val triangleIndices: List<Int>
```
The triangle indices that define the mesh faces. 
uv0 
```kotlin
val uv0: List<Vector2>?
```
Primary UV set. Optional. 
uv1 
```kotlin
val uv1: List<Vector2>?
```
Secondary UV set. Optional.