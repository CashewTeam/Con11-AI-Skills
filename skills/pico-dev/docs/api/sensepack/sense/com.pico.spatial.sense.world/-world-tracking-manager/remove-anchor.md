# removeAnchor | PICO Spatial SDK

sense / com.pico.spatial.sense.world / WorldTrackingManager / removeAnchor 
# removeAnchor
```kotlin
suspend fun removeAnchor(uuid: UUID): WorldTrackingResult<Unit>
```
Asynchronously removes an anchor with the specified UUID. 
#### Return
The result indicating the success or failure of the removal. 
#### Parameters
uuid 
The UUID of the anchor to remove.