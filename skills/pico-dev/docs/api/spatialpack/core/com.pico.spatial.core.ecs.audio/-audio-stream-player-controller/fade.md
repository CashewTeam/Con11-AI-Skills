# fade | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamPlayerController / fade 
# fade
```kotlin
fun fade(targetVolume: Float = 1.0f, duration: Long, fadeMode: AudioInterpolatorType = AudioInterpolatorType.CUBIC): Boolean
```
Fade the audio to the specified volume over a specified duration. 
#### Return
true if fade successfully otherwise false. Note: if targetVolume or duration out of range, it will return false. 
#### Parameters
target Volume 
The target volume value range0.0, 1.0. 
duration 
The duration of the fade (in milliseconds). 
fade Mode 
The type of interpolation to use for the fade. 
#### See also
Audio Interpolator Type