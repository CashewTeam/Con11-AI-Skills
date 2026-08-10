# getDuration | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / getDuration 
# getDuration
```kotlin
fun getDuration(): Long
```
Gets the total duration of the video, in milliseconds. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
The duration of the video in milliseconds, or  -1  if retrieval fails.