# setVolume | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / setVolume 
# setVolume
```kotlin
fun setVolume(volume: Float): Boolean
```
Sets the volume for video playback. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the volume is set successfully;  false  otherwise. 
#### Parameters
volume 
The volume level to set. The valid value range is 0.0f, 1.0f.