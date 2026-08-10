# AudioMixerGroupResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioMixerGroupResource / AudioMixerGroupResource 
# AudioMixerGroupResource
```kotlin
constructor(name: String, volume: Float = 1.0f, playbackSpeed: Float = 1.0f)
```
Creates an  AudioMixerGroupResource  with a specified name, volume, and playback speed. 
Note: Due to Kotlin constructor rules, validation occurs after the underlying adapter is created. If validation fails, the resource is closed immediately. 
#### Parameters
name 
The group name. Must be alphanumeric and at most 256 bytes. 
volume 
Initial volume in the range 0.0f, 1.0f. Default is  1.0f . 
playback Speed 
Initial playback speed in the range (0.25f, 4.0f]. Default is  1.0f . 
#### Throws
Illegal Argument Exception 
If  name  is invalid or exceeds the maximum length.