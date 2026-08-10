# release | PICO Spatial SDK

core / com.pico.spatial.audio / SpatialAudioTrackExtension / release 
# release
```kotlin
@MainThread
```fun  release ( ) 
Releases all resources associated with this spatial audio extension. 
When to call : Call this method when you are done with the current attachment (e.g., when stopping playback, switching to a different audio source, or destroying the parent Entity). After calling  release , the same  SpatialAudioTrackExtension  instance can be reused for a new attachment. 
Note : This method does not release or stop the AudioTrack itself. Releasing the AudioTrack remains the caller's responsibility.