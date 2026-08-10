# loadAllAnchors | PICO Spatial SDK

sense / com.pico.spatial.sense.mesh / MeshTrackingManager / loadAllAnchors 
# loadAllAnchors
```kotlin
suspend fun loadAllAnchors(): Array<MeshAnchor>
```
Loads all mesh anchors asynchronously. 
This function retrieves all currently tracked mesh anchors. It is only available when the tracking manager is in the running state. 
#### Return
A suspend function that returns an array of  MeshAnchor  objects. If the tracking manager is not running, an empty array is returned.