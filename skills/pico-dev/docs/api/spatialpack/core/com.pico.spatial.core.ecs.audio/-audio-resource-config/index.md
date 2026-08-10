# AudioResourceConfig | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioResourceConfig 
# AudioResourceConfig
```kotlin
class AudioResourceConfig(mixerGroupID: String, ambisonicsType: AmbisonicsType = AmbisonicsType.NONE)
```
The configuration of  com.pico.spatial.core.ecs.resource.AudioResource . This class is used to configure the audio resource with a mix group name which is hold by  com.pico.spatial.core.ecs.resource.AudioMixerGroupResource  which will be used by  com.pico.spatial.core.ecs.AudioMixerGroupsComponent . The  mixerGroupID  can link  com.pico.spatial.core.ecs.resource.AudioResource , com.pico.spatial.core.ecs.resource.AudioMixerGroupResource  and  com.pico.spatial.core.ecs.AudioMixerGroupsComponent  together, so that user can control the volume and playbackRate of the audio resources as a group. 
#### Parameters
mixer Group ID 
The name of the mix group. 
ambisonics Type 
The ambisonics audio type of the current audio resource. 
Members 
## Constructors
Audio Resource Config 
```kotlin
constructor(mixerGroupID: String, ambisonicsType: AmbisonicsType = AmbisonicsType.NONE)
```
```kotlin
constructor(mixerGroupID: String, ambisonicsType: AmbisonicsType = AmbisonicsType.NONE, randomStart: Boolean = false, loopEnable: Boolean = false)
```
Configuration class for  com.pico.spatial.core.ecs.resource.AudioResource . 
## Properties
ambisonics Type 
```kotlin
val ambisonicsType: AmbisonicsType
```
The ambisonics audio type of the audio resource. 
loop Enable 
```kotlin
val loopEnable: Boolean
```
Whether the audio resource should playback in loop mode. 
mixer Group ID 
```kotlin
val mixerGroupID: String
```
The identifier of the mixer group to which this audio resource belongs. 
random Start 
```kotlin
val randomStart: Boolean
```
Whether playback should begin at a random position within the audio resource's duration.