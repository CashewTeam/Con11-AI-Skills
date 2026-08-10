# setVolume | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamPlayerController / setVolume 
# setVolume
```kotlin
fun setVolume(@FloatRange(from = 0.0, to = 1.0) volume: Float = 1.0f): Boolean
```
Sets the playback volume. 
#### Return
true if setVolume successfully otherwise false. Note: if volume out of range, it will return false. 
#### Parameters
volume 
The audio volume value range0.0, 1.0.