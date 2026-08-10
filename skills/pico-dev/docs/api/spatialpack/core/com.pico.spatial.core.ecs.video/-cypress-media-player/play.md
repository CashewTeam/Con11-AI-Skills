# play | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / play 
# play
```kotlin
fun play(): Boolean
```
Starts video playback. 
Before calling this method, invoke  prepareAsync  and wait for the  CypressMediaPlayerCallback.onPrepared  callback. It’s recommended to call  play  within  onPrepared  to ensure the playback is fully prepared. It's also recommended to ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if the video plays successfully;  false  otherwise.