# getVolume | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / getVolume 
# getVolume
```kotlin
fun getVolume(): Float
```
Gets the volume of video playback. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
The volume of video playback, whose range is 0.0f, 1.0f, or  -1.0f  if retrieval fails.