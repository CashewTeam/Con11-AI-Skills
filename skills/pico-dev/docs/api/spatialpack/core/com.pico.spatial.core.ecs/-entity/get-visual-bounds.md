# getVisualBounds | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / getVisualBounds 
# getVisualBounds
```kotlin
@MainThread
```fun  getVisualBounds ( relativeTo :  Entity ? ,  recursive :  Boolean  =  true ,  enabledOnly :  Boolean  =  false ) :  BoundingBox 
Computes a bounding box for the entity in the specified space, optionally including child entities. 
#### Return
The bounding box. 
#### Parameters
relative To 
An entity that defines a frame of reference. Set to null to indicate  com.pico.spatial.core.container.SpatialContainer . 
recursive 
A Boolean that specifies whether to incorporate the bounds of all descendants of this Entity. 
enabled Only 
A Boolean that specifies whether to incorporate only the bounds of all enabled entities, including this entity itself and its descendants.