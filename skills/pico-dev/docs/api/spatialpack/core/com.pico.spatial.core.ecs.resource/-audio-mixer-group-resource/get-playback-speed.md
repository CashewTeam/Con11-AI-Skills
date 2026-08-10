# getPlaybackSpeed | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioMixerGroupResource / getPlaybackSpeed 
# getPlaybackSpeed
```kotlin
fun getPlaybackSpeed(): Float
```
Gets the playback speed of this  AudioMixerGroupResource . 
#### Return
The current playback speed in (0.25f, 4.0f]. 
#### Throws
Illegal State Exception 
If this resource has been closed.