# ChannelAudioComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / ChannelAudioComponent / ChannelAudioComponent 
# ChannelAudioComponent
```kotlin
constructor()
```
Creates a  ChannelAudioComponent  instance with empty settings. 
```kotlin
constructor(@FloatRange(from = 0.0, to = 1.0) volume: Float = 1.0f)
```
Creates a  ChannelAudioComponent  with an initial volume. 
Note: The value must be within  [0.0, 1.0] , otherwise an  IllegalArgumentException  is thrown. Defaults to  1.0f  when not provided. 
#### Parameters
volume 
Initial volume in  [0.0, 1.0] , default  1.0f . 
#### Throws
Illegal Argument Exception 
if the volume is not in the range  [0.0, 1.0] .