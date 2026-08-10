# AmbientAudioComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AmbientAudioComponent / AmbientAudioComponent 
# AmbientAudioComponent
```kotlin
constructor()
```
Creates a new  AmbientAudioComponent  with default settings. 
```kotlin
constructor(@FloatRange(from = 0.0, to = 1.0) volume: Float = 1.0f, ambientOrientationMode: AmbientOrientationMode = AmbientOrientationMode.ORIENTATION_ONLY)
```
Creates an  AmbientAudioComponent  instance with the specified volume and ambient orientation mode. 
#### Parameters
volume 
The volume to set. The valid value range is  [0.0, 1.0] . The default value is  1.0f . If the specified volume value is not in the valid range, the default value will be used. 
ambient Orientation Mode 
The ambient orientation mode for audio. The default value is  AmbientOrientationMode.ORIENTATION_ONLY . 
#### Throws
Illegal Argument Exception 
if the volume is not in the range  [0.0, 1.0] .