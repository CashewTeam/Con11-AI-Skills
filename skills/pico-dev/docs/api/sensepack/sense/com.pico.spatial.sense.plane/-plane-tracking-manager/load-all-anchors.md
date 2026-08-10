# loadAllAnchors | PICO Spatial SDK

sense / com.pico.spatial.sense.plane / PlaneTrackingManager / loadAllAnchors 
# loadAllAnchors
```kotlin
suspend fun loadAllAnchors(): Array<PlaneAnchor>
```
Loads all Plane anchors asynchronously. 
This function retrieves all currently tracked Plane anchors. It is only available when the tracking manager is in the running state. 
#### Return
A suspend function that returns an array of  PlaneAnchor  objects. If the tracking manager is not running, an empty array is returned.