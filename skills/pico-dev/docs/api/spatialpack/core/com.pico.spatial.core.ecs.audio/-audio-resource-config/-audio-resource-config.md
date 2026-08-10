# AudioResourceConfig | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioResourceConfig / AudioResourceConfig 
# AudioResourceConfig
```kotlin
constructor(mixerGroupID: String, ambisonicsType: AmbisonicsType = AmbisonicsType.NONE)
```
#### Parameters
mixer Group ID 
The name of the mix group. 
ambisonics Type 
The ambisonics audio type of the current audio resource. 
```kotlin
constructor(mixerGroupID: String, ambisonicsType: AmbisonicsType = AmbisonicsType.NONE, randomStart: Boolean = false, loopEnable: Boolean = false)
```
Configuration class for  com.pico.spatial.core.ecs.resource.AudioResource . 
This class provides configuration options for audio resources, including mixer group assignment, playback behavior settings, and ambisonics audio format specification. The configuration enables integration with  com.pico.spatial.core.ecs.resource.AudioMixerGroupResource  and  com.pico.spatial.core.ecs.AudioMixerGroupsComponent  for group-based audio control. 
The mixer group identified by  mixerGroupID  serves as the linkage between audio resources, mixer group resources, and mixer group components, allowing users to control volume and playback rate for multiple audio resources as a unified group. 
#### Parameters
mixer Group ID 
The identifier of the mixer group to which this audio resource belongs. This identifier links the audio resource to a specific  com.pico.spatial.core.ecs.resource.AudioMixerGroupResource  and enables group-based audio control through  com.pico.spatial.core.ecs.AudioMixerGroupsComponent . 
ambisonics Type 
Specifies the ambisonics audio format for this audio resource. Ambisonics is a full-sphere surround sound format that enables spatial audio reproduction in multiple directions. The default value is  AmbisonicsType.NONE , indicating that the audio resource does not utilize ambisonics encoding. 
random Start 
Indicates whether playback should begin at a random position within the audio resource's duration. When set to  true , each playback instance will start at a randomly selected position. Defaults to  false . 
loop Enable 
Specifies whether the audio resource should playback in loop mode. When set to  true , the audio will automatically repeat upon reaching the end of its duration. Defaults to  false .