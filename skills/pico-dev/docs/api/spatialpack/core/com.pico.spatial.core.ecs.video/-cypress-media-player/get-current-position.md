# getCurrentPosition | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / getCurrentPosition 
# getCurrentPosition
```kotlin
fun getCurrentPosition(): Long
```
Gets the current playback position of the video in milliseconds. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
The current position in milliseconds, or  -1  if retrieval fails.