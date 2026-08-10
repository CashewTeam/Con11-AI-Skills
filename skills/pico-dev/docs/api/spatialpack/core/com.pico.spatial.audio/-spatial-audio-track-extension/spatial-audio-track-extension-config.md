# spatialAudioTrackExtensionConfig | PICO Spatial SDK

core / com.pico.spatial.audio / SpatialAudioTrackExtension / spatialAudioTrackExtensionConfig 
# spatialAudioTrackExtensionConfig
```kotlin
fun spatialAudioTrackExtensionConfig(mode: SpatialAudioTrackExtension.SpatialAudioMode = SpatialAudioMode.AMBIENT, isAmbisonic: Boolean = false, builder: AudioTrack.Builder)
```
Configures spatial audio parameters on the  AudioTrack.Builder . 
When to call : Call this method before  AudioTrack.Builder.build  when using  withBuilder  attachment methods. The configuration is written into the Builder and affects the spatialization behavior of the resulting AudioTrack. 
Note : Call this method before using any attachment method to ensure the spatial audio mode is properly configured. 
#### Parameters
mode 
The spatial audio mode, defaults to  SpatialAudioMode.AMBIENT . 
is Ambisonic 
Whether the content is ambisonic encoded, defaults to false. 
builder 
The  AudioTrack.Builder  to configure. 
#### Throws
Illegal State Exception 
if configuration fails.