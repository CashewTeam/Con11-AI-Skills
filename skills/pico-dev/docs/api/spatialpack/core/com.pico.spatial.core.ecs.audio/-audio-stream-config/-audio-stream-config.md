# AudioStreamConfig | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamConfig / AudioStreamConfig 
# AudioStreamConfig
```kotlin
constructor(channelLayoutType: AudioChannelLayoutType = AudioChannelLayoutType.STANDARD, audioMixerGroupId: String = "", channelLayout: AudioChannelLayout = AudioChannelLayout.OUTPUT_LAYOUT_STEREO, ambisonicType: AmbisonicsType = AmbisonicsType.NONE, audioFormat: AudioFormat = AudioFormat())
```
Constructs an audio stream configuration for playback control. 
#### Parameters
channel Layout Type 
Specifies audio spatialization mode:     - AudioChannelLayoutType.STANDARD for traditional layouts (stereo, 5.1, etc.).     - AudioChannelLayoutType.AMBISONICS for spherical harmonic-based audio. 
audio Mixer Group Id 
Audio group identifier for volume/mixing control. 
channel Layout 
Required when using STANDARD layout:     - Must be non-null if channelLayoutType is STANDARD.     - Specify channel arrangement (e.g. OUTPUT_LAYOUT_5_1_2). 
ambisonic Type 
Required when using AMBISONICS layout:     - Must be non-null if channelLayoutType is AMBISONICS.     - Specify Ambisonics format (e.g. ACN_SN3D_1). 
audio Format 
PCM format details including:     - Sample rate (e.g. 48000).     - Bit depth.     - Channel count. 
Usage example: 

```
// STANDARD configurationAudioStreamConfig(    AudioChannelLayoutType.STANDARD,    "game_effects",    AudioChannelLayout.OUTPUT_LAYOUT_STEREO,    AmbisonicsType.NONE,    AudioFormat(sampleRate = 48000))// AMBISONICS configurationAudioStreamConfig(    AudioChannelLayoutType.AMBISONICS,    "environment",    AudioChannelLayout.OUTPUT_LAYOUT_INVALID,    AmbisonicsType.ACN_SN3D_2,    AudioFormat(sampleRate = 96000))
```
#### Throws
Illegal State Exception 
if configuration parameters are invalid:     - When channelLayoutType is AudioChannelLayoutType.STANDARD and channelLayout is       AudioChannelLayout.OUTPUT_LAYOUT_INVALID.     - When channelLayoutType is AudioChannelLayoutType.AMBISONICS and ambisonicType is       AmbisonicsType.NONE.