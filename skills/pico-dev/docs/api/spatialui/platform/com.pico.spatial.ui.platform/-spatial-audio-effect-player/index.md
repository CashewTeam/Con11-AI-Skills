# SpatialAudioEffectPlayer | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / SpatialAudioEffectPlayer 
# SpatialAudioEffectPlayer
```kotlin
interface SpatialAudioEffectPlayer
```
Player for spatial audio effects. we will provider the default implementation. callers should use  LocalAudioEffectPlayer  to get the instance. 
Members 
## Functions
play System 
```kotlin
abstract fun playSystem(soundEffect: SpatialSoundEffect)
```
Plays the system sound effect.