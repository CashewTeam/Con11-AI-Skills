# setPlaybackSpeed | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamPlayerController / setPlaybackSpeed 
# setPlaybackSpeed
```kotlin
fun setPlaybackSpeed(rate: Float): Boolean
```
Set the audio playback speed. 
#### Return
true if setPlaybackSpeed successfully otherwise false. Note: if rate out of range, it will return false. 
#### Parameters
rate 
The audio playback speed rate range0.25, 4.