# getPlaybackSpeed | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / getPlaybackSpeed 
# getPlaybackSpeed
```kotlin
fun getPlaybackSpeed(): Float
```
Gets the playback speed of the player. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
The playback speed of the video, whose range is 0.5f, 4.0f, or  -1f  if retrieval fails.