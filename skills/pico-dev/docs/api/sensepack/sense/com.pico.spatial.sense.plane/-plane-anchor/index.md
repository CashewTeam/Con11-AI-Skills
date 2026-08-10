# PlaneAnchor | PICO Spatial SDK

sense / com.pico.spatial.sense.plane / PlaneAnchor 
# PlaneAnchor
```kotlin
@RequiredFullSpace
```class  PlaneAnchor  :  Anchor 
Represents a plane anchor in 3D space with a unique identifier, transform properties, and additional mesh-related data. 
The  PlaneAnchor  class is designed to encapsulate the representation of a detected plane or surface in 3D space. It includes positional and rotational information, as well as detailed mesh geometry and metadata. This makes it particularly useful for applications involving spatial mapping, object tracking, or augmented reality scenarios where precise plane detection and visualization are required. 
Members 
## Properties
anchor UUID 
```kotlin
val anchorUUID: UUID
```
The UUID ensures that each anchor is uniquely identifiable within the application. 
bounding Box Size 
```kotlin
val boundingBoxSize: Vector2
```
The size of the axis-aligned bounding box (AABB) of the anchor in 2D space. 
indices 
```kotlin
val indices: List<Int>
```
A list of indices that define the connectivity of the vertices in the mesh. 
plane Orientation 
```kotlin
val planeOrientation: PlaneOrientation
```
The orientation of the plane anchor. 
semantics 
```kotlin
val semantics: SemanticLabelType
```
The semantic data associated with the plane anchor. 
transform 
```kotlin
val transform: Transform
```
The transform of the anchor, combining position, rotation, and scale. The default scale is always Vector3(1f, 1f, 1f). 
vertices 
```kotlin
val vertices: List<Vector3>
```
A list of vertices that define the geometry of the plane anchor. 
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