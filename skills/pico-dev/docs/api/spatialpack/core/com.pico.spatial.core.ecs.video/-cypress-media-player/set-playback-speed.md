# setPlaybackSpeed | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / setPlaybackSpeed 
# setPlaybackSpeed
```kotlin
fun setPlaybackSpeed(speed: Float): Boolean
```
Sets the speed for video playback. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the playback speed is set successfully;  false  otherwise. 
#### Parameters
speed 
The playback speed to set. The valid value range is 0.5f, 4.0f. The default value is  1.0f .