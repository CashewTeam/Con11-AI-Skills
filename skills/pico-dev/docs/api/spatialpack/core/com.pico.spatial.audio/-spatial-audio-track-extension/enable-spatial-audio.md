# enableSpatialAudio | PICO Spatial SDK

core / com.pico.spatial.audio / SpatialAudioTrackExtension / enableSpatialAudio 
# enableSpatialAudio
```kotlin
fun enableSpatialAudio(enable: Boolean, audioTrack: AudioTrack): Boolean
```
Enables or disables spatial audio processing for the given  AudioTrack . 
When to use : Call this method at runtime to toggle the spatializer effect on or off after the AudioTrack has already been attached (via any  attachTo*  method). This is useful for scenarios such as: 
- 
Toggling spatial audio on/off via a user settings switch. 
- 
Temporarily disabling spatialization during certain playback states. 
#### Return
true if the operation succeeded, false otherwise. 
#### Parameters
enable 
true to enable spatial audio, false to disable. 
audio Track 
The  AudioTrack  to enable/disable spatial audio on.