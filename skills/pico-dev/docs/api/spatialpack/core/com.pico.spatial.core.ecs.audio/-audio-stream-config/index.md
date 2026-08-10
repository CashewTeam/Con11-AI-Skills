# AudioStreamConfig | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamConfig 
# AudioStreamConfig
```kotlin
class AudioStreamConfig
```
Configuration class for pcm audio stream playback and data handling. 
This class encapsulates all necessary parameters for configuring an audio stream player in the ECS system, including channel layout specifications, audio format details, and data delivery mode selection. 
Key features: 
- 
Supports both push and pull modes for audio data delivery 
- 
Handles standard and Ambisonics channel layouts 
- 
Manages audio format specifications including sample rate and channel configuration 
- 
Integrates with the audio mix group system for volume control 
Usage example: 

```
// STANDARD configval standardConfig = AudioStreamConfig(    AudioChannelLayoutType.STANDARD,    "mix_group_1",    AudioChannelLayout.OUTPUT_LAYOUT_STEREO,    AmbisonicsType.NONE,    AudioFormat(sampleRate = 48000),    null)// AMBISONICS configval ambisonicConfig = AudioStreamConfig(    AudioChannelLayoutType.AMBISONICS,    "mix_group_2",    AudioChannelLayout.OUTPUT_LAYOUT_INVALID,    AmbisonicsType.ACN_SN3D_1,    AudioFormat(sampleRate = 96000))
```Members 
## Constructors
Audio Stream Config 
```kotlin
constructor(channelLayoutType: AudioChannelLayoutType = AudioChannelLayoutType.STANDARD, audioMixerGroupId: String = "", channelLayout: AudioChannelLayout = AudioChannelLayout.OUTPUT_LAYOUT_STEREO, ambisonicType: AmbisonicsType = AmbisonicsType.NONE, audioFormat: AudioFormat = AudioFormat())
```
Constructs an audio stream configuration for playback control. 
## Properties
ambisonics Type 
```kotlin
val ambisonicsType: AmbisonicsType
```
Ambisonics format specification (when using Ambisonics layout). 
audio Channel Count 
```kotlin
val audioChannelCount: Int
```
Number of audio channels per frame. 
audio Format 
```kotlin
val audioFormat: AudioFormat?
```
PCM audio format configuration including sample rate and bit depth. 
channel Layout 
```kotlin
val channelLayout: AudioChannelLayout
```
Detailed channel arrangement configuration. 
channel Layout Type 
```kotlin
val channelLayoutType: AudioChannelLayoutType
```
Specifies standard or Ambisonics layout type. 
mixer Group ID 
```kotlin
val mixerGroupID: String?
```
Identifier for audio mix grouping (volume control purposes). 
valid 
```kotlin
@get:JvmName(name = "isValid")
```val  valid :  Boolean 
The controller is valid.