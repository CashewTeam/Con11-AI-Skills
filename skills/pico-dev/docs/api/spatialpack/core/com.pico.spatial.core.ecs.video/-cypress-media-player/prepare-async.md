# prepareAsync | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / prepareAsync 
# prepareAsync
```kotlin
fun prepareAsync(): Boolean
```
Asynchronously prepares the video for playback. 
This method sets up the video for playback in the background. Once preparation is complete, the  CypressMediaPlayerCallback.onPrepared  callback will be triggered. To ensure  play()  is called at the correct time, invoke the  play()  method within the  CypressMediaPlayerCallback.onPrepared  callback. Make sure to implement and register this callback with the player upon its creation. 
Ensure the player is valid before calling this method, otherwise it will throw an  IllegalStateException . 
#### Return
true  if preparation is successful;  false  otherwise.