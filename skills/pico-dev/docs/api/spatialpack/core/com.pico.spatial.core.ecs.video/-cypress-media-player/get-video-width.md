# getVideoWidth | PICO Spatial SDK

core / com.pico.spatial.core.ecs.video / CypressMediaPlayer / getVideoWidth 
# getVideoWidth
```kotlin
fun getVideoWidth(): Int
```
Gets the width of the currently configured video data source. 
#### Return
the width of the video, or 0 if there is no video, no display surface has been set, or the width has not yet been determined. Once the  CypressMediaPlayer  is prepared, you can obtain the real-time video width. You can register a  CypressMediaPlayerCallback  via  registerCypressMediaPlayerCallback  to receive a notification when  CypressMediaPlayer  is prepared and the width becomes available.