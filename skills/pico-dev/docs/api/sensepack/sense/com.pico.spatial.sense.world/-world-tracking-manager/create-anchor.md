# createAnchor | PICO Spatial SDK

sense / com.pico.spatial.sense.world / WorldTrackingManager / createAnchor 
# createAnchor
```kotlin
suspend fun createAnchor(position: Vector3, rotation: EulerAngles, name: String = ""): WorldTrackingResult<WorldAnchor>
```
Asynchronously creates a new anchor with a specified position, rotation, and name. 
This method enables you to create a new anchor in the 3D space defined by the current Stage. 
#### Return
The result containing the created WorldAnchor. 
#### Parameters
position 
The position of the anchor in the coordinate space of the current Stage. 
rotation 
The rotation of the anchor in the coordinate space of the current Stage. 
name 
(Optional) The name of the anchor, which defaults to an empty string.