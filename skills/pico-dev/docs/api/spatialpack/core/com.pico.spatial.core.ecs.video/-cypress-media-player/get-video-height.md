# getVideoHeight | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / getVideoHeight 
# getVideoHeight
```kotlin
fun getVideoHeight(): Int
```
Gets the height of the currently configured video data source. 
#### Return
the height of the video, or 0 if there is no video, no display surface has been set, or the height has not yet been determined. Once the  CypressMediaPlayer  is prepared, you can obtain the real-time video height. You can register a  CypressMediaPlayerCallback  via  registerCypressMediaPlayerCallback  to receive a notification when  CypressMediaPlayer  is prepared and the height becomes available.