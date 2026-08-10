# attachToEntityWithBuilder | PICO Spatial SDK

core / com.pico.spatial.audio / SpatialAudioTrackExtension / attachToEntityWithBuilder 
# attachToEntityWithBuilder
```kotlin
@MainThread
```fun  attachToEntityWithBuilder ( entityToAttach :  Entity ,  builder :  AudioTrack.Builder ) 
Attaches spatial audio to an Entity using a pre-configured  AudioTrack.Builder . 
When to use : Use this method when you control the AudioTrack creation pipeline and can configure the Builder before calling  build() . The audio will follow the target Entity's position in 3D space. 
Usage steps : 
- 
Configure spatial audio mode via  spatialAudioTrackExtensionConfig . 
- 
Call this method with the target entity and the configured builder. 
- 
Build the AudioTrack:  builder.build() . 
#### Parameters
entity To Attach 
The entity to attach spatial audio to. 
builder 
The  AudioTrack.Builder  with spatial audio configuration (must be pre-configured via  spatialAudioTrackExtensionConfig ). 
#### Throws
Illegal State Exception 
if attachment fails.