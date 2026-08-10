# semantics | PICO Spatial SDK

sense / com.pico.spatial.sense.mesh / MeshAnchor / semantics 
# semantics
```kotlin
val semantics: List<SemanticLabelType>
```
The semantic data associated with the mesh anchor. 
This property provides a list of semantic types that describe the elements or regions represented by the mesh anchor. Since a mesh anchor operates on a per-vertex basis, it can encompass multiple semantic types simultaneously. For example, a single mesh anchor might represent areas of a wall, floor, and door within the same spatial region.