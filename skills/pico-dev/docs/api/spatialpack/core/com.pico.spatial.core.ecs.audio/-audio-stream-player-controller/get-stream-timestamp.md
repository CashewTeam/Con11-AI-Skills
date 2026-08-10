# getStreamTimestamp | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamPlayerController / getStreamTimestamp 
# getStreamTimestamp
```kotlin
@ExperimentalSpatialApi
```fun  getStreamTimestamp ( ) :  AudioStreamTimestamp ? 
Retrieves high-precision playback timing information. 
#### Return
Null if unavailable, otherwise contains:     - framePosition: Current 0-based audio frame index.     - timeNs: Monotonic clock timestamp (nanoseconds). 
Usage note: Timestamps remain valid until next audio buffer processing.