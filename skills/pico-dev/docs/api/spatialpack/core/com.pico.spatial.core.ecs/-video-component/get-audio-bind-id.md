# getAudioBindId | PICO Spatial SDK

core / com.pico.spatial.core.ecs / VideoComponent / getAudioBindId 
# getAudioBindId
```kotlin
fun getAudioBindId(): Long?
```
Gets the audio binding ID when using  VideoComponent  to play video with spatial audio effects. 
This function retrieves the audio binding ID, which allows the audio player to bind the spatial audio effect to the entity that has the  VideoComponent . 
#### Return
The audio binding ID if successful, null for failure.