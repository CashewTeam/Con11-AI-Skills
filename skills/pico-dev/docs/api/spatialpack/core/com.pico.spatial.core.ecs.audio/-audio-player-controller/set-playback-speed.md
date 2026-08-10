# setPlaybackSpeed | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioPlayerController / setPlaybackSpeed 
# setPlaybackSpeed
```kotlin
fun setPlaybackSpeed(rate: Float): Boolean
```
Sets the playback speed for the audio. 
#### Return
true  if the speed is set successfully;  false  otherwise. If the specified speed is out of the valid range,  false  will be returned. 
#### Parameters
rate 
The audio playback speed. The valid value range is 0.25, 4.