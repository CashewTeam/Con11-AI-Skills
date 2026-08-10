# stop | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / stop 
# stop
```kotlin
fun stop(): Boolean
```
Stops video playback. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the video stops successfully;  false  otherwise.