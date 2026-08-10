# attachToContainerWithBuilder | PICO Spatial SDK

core / com.pico.spatial.audio / SpatialAudioTrackExtension / attachToContainerWithBuilder 
# attachToContainerWithBuilder
```kotlin
fun attachToContainerWithBuilder(currentContext: Context, builder: AudioTrack.Builder)
```
Attaches spatial audio to a Container/Context using a pre-configured  AudioTrack.Builder . 
When to use : Use this method when the audio should follow the window/container position rather than a specific Entity. This is suitable for window-based playback scenarios (e.g., fixed-position background audio). 
Usage steps : 
- 
Configure spatial audio mode via  spatialAudioTrackExtensionConfig . 
- 
Call this method with the configured builder. 
- 
Build the AudioTrack:  audioTrackBuilder.build() . 
#### Parameters
current Context 
The Context/Container to attach spatial audio to. 
builder 
The  AudioTrack.Builder  with spatial audio configuration (must be pre-configured via  spatialAudioTrackExtensionConfig ). 
#### Throws
Illegal State Exception 
if attachment fails.