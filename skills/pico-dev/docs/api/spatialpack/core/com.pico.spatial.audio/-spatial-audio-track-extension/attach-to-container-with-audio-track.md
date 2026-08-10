# attachToContainerWithAudioTrack | PICO Spatial SDK

core / com.pico.spatial.audio / SpatialAudioTrackExtension / attachToContainerWithAudioTrack 
# attachToContainerWithAudioTrack
```kotlin
fun attachToContainerWithAudioTrack(currentContext: Context, audioTrack: AudioTrack)
```
Attaches spatial audio to a Container/Context using an already-created  AudioTrack . 
When to use : Use this method when the  AudioTrack  is already created by an external framework and the audio should follow the window/container position in 3D space. 
Usage steps : 
- 
Configure spatial audio mode via  spatialAudioTrackExtensionConfig  before creating the     AudioTrack. 
- 
Create/configure the  AudioTrack  through your media framework. 
- 
Call this method to bind the AudioTrack to the container/window. 
#### Parameters
current Context 
The Context/Container to attach spatial audio to. 
audio Track 
The  AudioTrack  to bind. 
#### Throws
Illegal State Exception 
if attachment fails.