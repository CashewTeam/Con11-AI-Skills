# SpatialTapValue | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / SpatialTapValue / SpatialTapValue 
# SpatialTapValue
```kotlin
constructor(position: Offset3D, interactionKind: InteractionKind, targetEntity: Entity? = null)
```
#### Parameters
position 
The position in pixels where a spatial tap happens. And the position 3d value is under view local coordinate. 
interaction Kind 
The interaction kind of the tap gesture. 
target Entity 
The target entity of the tap gesture. When user tap 3d model, targetEntity is the 3d model entity. And it is null when user tap 2d view.