# seekTo | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / seekTo 
# seekTo
```kotlin
fun seekTo(time: Long): Boolean
```
Seeks to the specified position in the video. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the seek operation is successful;  false  otherwise. 
#### Parameters
time 
The target position (in milliseconds) to seek to.