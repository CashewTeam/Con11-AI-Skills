# isPlaying | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / isPlaying 
# isPlaying
```kotlin
fun isPlaying(): Boolean
```
Checks whether the video is currently playing. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the video is playing;  false  otherwise.