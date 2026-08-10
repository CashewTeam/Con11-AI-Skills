# com.pico.spatial.core.ecs.audio | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio 
# Package-level declarations
Types 
## Types
Ambient Orientation Mode 
```kotlin
enum AmbientOrientationMode : Enum<AmbientOrientationMode>
```
Defines how ambient audio orientation is applied to the audio source. 
Ambisonics Type 
```kotlin
enum AmbisonicsType : Enum<AmbisonicsType>
```
Defines Ambisonics audio formats for spatial audio processing. 
Audio Channel Layout 
```kotlin
enum AudioChannelLayout : Enum<AudioChannelLayout>
```
Defines standard audio channel layouts for spatial audio configurations. 
Audio Channel Layout Type 
```kotlin
enum AudioChannelLayoutType : Enum<AudioChannelLayoutType>
```
Defines the fundamental spatial audio rendering mode for audio streams. 
Audio Format 
```kotlin
class AudioFormat
```
Represents audio format configuration for spatial audio processing. 
Audio Group Resource Play Mode 
```kotlin
enum AudioGroupResourcePlayMode : Enum<AudioGroupResourcePlayMode>
```
Audio group resource play mode. 
Audio Interpolator Type 
```kotlin
enum AudioInterpolatorType : Enum<AudioInterpolatorType>
```
AudioInterpolatorType is an enum that represents the fade type of how to fade the audio to the target volume during the fade operation by AudioPlayerController. 
Audio Player Controller 
```kotlin
class AudioPlayerController : Closeable
```
A handle that is used to control audio playback，including playing, pausing, resuming, stopping an audio, and checking the playback status of an audio. 
Audio Resource Config 
```kotlin
class AudioResourceConfig(mixerGroupID: String, ambisonicsType: AmbisonicsType = AmbisonicsType.NONE)
```
The configuration of  com.pico.spatial.core.ecs.resource.AudioResource . This class is used to configure the audio resource with a mix group name which is hold by  com.pico.spatial.core.ecs.resource.AudioMixerGroupResource  which will be used by  com.pico.spatial.core.ecs.AudioMixerGroupsComponent . The  mixerGroupID  can link  com.pico.spatial.core.ecs.resource.AudioResource , com.pico.spatial.core.ecs.resource.AudioMixerGroupResource  and  com.pico.spatial.core.ecs.AudioMixerGroupsComponent  together, so that user can control the volume and playbackRate of the audio resources as a group. 
Audio Stream Buffer Data 
```kotlin
class AudioStreamBufferData
```
Container for streaming audio data buffers provided during  AudioStreamDataCallback  execution. 
Audio Stream Config 
```kotlin
class AudioStreamConfig
```
Configuration class for pcm audio stream playback and data handling. 
Audio Stream Data Callback 
```kotlin
interface AudioStreamDataCallback
```
Callback interface for providing audio stream data in pull mode. 
Audio Stream Player Controller 
```kotlin
class AudioStreamPlayerController : Closeable
```
Central controller for managing PCM audio stream playback. 
Audio Stream Timestamp 
```kotlin
class AudioStreamTimestamp
```
Represents precise timing information for audio stream playback. 
Directivity 
```kotlin
class Directivity
```
Defines how sound is emitted from an audio source and perceived within the spatial environment. 
Distance Attenuation Mode 
```kotlin
enum DistanceAttenuationMode : Enum<DistanceAttenuationMode>
```
Defines how audio volume attenuates as the distance from the audio source increases.