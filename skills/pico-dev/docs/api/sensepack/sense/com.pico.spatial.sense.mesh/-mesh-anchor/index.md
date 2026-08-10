# MeshAnchor | PICO Spatial SDK

sense / com.pico.spatial.sense.mesh / MeshAnchor 
# MeshAnchor
```kotlin
@RequiredFullSpace
```class  MeshAnchor  :  Anchor 
Represents a mesh anchor with a unique identifier, position, rotation, and additional mesh-specific data. 
This class is used to define an anchor in 3D space that includes its position, orientation, and detailed information about the mesh it represents. A mesh anchor is particularly useful in scenarios where a physical object or surface is scanned, and its geometry, along with associated metadata, needs to be processed or visualized within the application. 
Members 
## Properties
anchor UUID 
```kotlin
val anchorUUID: UUID
```
The UUID ensures that each anchor is uniquely identifiable within the application. 
bounding Box Size 
```kotlin
val boundingBoxSize: Vector3
```
The size of the axis-aligned bounding box (AABB) of the anchor. 
indices 
```kotlin
val indices: List<Int>
```
A list of indices that define the connectivity of the vertices in the mesh. 
semantics 
```kotlin
val semantics: List<SemanticLabelType>
```
The semantic data associated with the mesh anchor. 
transform 
```kotlin
val transform: Transform
```
The transform of the anchor, combining position, rotation, and scale. The default scale is always Vector3(1f, 1f, 1f). 
vertices 
```kotlin
val vertices: List<Vector3>
```
A list of vertices that define the geometry of the mesh anchor. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```