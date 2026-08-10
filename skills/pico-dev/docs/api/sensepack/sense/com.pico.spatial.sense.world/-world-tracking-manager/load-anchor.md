# loadAnchor | PICO Spatial SDK

sense / com.pico.spatial.sense.world / WorldTrackingManager / loadAnchor 
# loadAnchor
```kotlin
suspend fun loadAnchor(uuids: Array<UUID> = arrayOf()): WorldTrackingResult<Array<WorldAnchor>>
```
Asynchronously loads anchors with the specified UUIDs. 
#### Return
The  WorldTrackingResult  containing an array of loaded WorldAnchors. 
#### Parameters
uuids 
An array of UUIDs identifying the anchors to load. If empty, all available anchors will be loaded.