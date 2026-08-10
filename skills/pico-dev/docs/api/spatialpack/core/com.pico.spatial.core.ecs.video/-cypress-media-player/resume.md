# resume | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / resume 
# resume
```kotlin
fun resume(): Boolean
```
Resumes video playback. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the video resumes successfully;  false  otherwise.