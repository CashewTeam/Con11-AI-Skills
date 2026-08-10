# attachToEntityWithAudioTrack | PICO Spatial SDK

core / com.pico.spatial.audio / SpatialAudioTrackExtension / attachToEntityWithAudioTrack 
# attachToEntityWithAudioTrack
```kotlin
@MainThread
```fun  attachToEntityWithAudioTrack ( entityToAttach :  Entity ,  audioTrack :  AudioTrack ) 
Attaches spatial audio to an Entity using an already-created  AudioTrack . 
When to use : Use this method when the  AudioTrack  is already created by an external framework (e.g., ExoPlayer, MediaPlayer) and you cannot control the Builder phase. The AudioTrack is immediately bound to the target Entity's position. 
Usage steps : 
- 
Configure spatial audio mode via  spatialAudioTrackExtensionConfig  before creating the     AudioTrack. 
- 
Create/configure the  AudioTrack  through your media framework. 
- 
Call this method to bind the AudioTrack to the target Entity's position. 
#### Parameters
entity To Attach 
The entity to attach spatial audio to. 
audio Track 
The  AudioTrack  to bind. 
#### Throws
Illegal State Exception 
if attachment fails.