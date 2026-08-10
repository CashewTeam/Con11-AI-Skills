# pause | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / pause 
# pause
```kotlin
fun pause(): Boolean
```
Pauses video playback. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the video pauses successfully;  false  otherwise.