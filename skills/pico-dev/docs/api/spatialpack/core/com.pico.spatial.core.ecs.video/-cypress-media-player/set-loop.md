# setLoop | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / setLoop 
# setLoop
```kotlin
fun setLoop(loop: Boolean): Boolean
```
Sets the loop mode for video playback. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the loop mode is set successfully;  false  otherwise. 
#### Parameters
loop 
true  to enable looping;  false  to disable it.