# AudioGroupResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioGroupResource 
# AudioGroupResource
```kotlin
class AudioGroupResource : AudioAsset
```
The  AudioAsset  type for audio group. 
AudioGroupResource is a resource that can be used to group audio resources. It allows you to create collections of audio resources that can be played back in different modes (random, forward sequence, backward sequence). 
This class extends  AudioAsset  and provides functionality to manage a group of  AudioResource  objects. The group can be used to play multiple audio files in a specific order or randomly based on the configured  AudioGroupResourcePlayMode . 
#### See also
Audio Resource Audio Group Resource Play Mode Audio Asset Members 
## Constructors
Audio Group Resource 
```kotlin
constructor(name: String, audioResources: List<AudioResource>, mode: AudioGroupResourcePlayMode = AudioGroupResourcePlayMode.FORWARD)
```
Creates an AudioGroupResource from a list of AudioResources. 
## Properties
audio Resources 
```kotlin
val audioResources: List<AudioResource>
```
Gets the list of all AudioResources in this audio group. 
## Functions
close 
```kotlin
open override fun close()
```
Closes this audio group resource and releases any native resources. 
get Name 
```kotlin
fun getName(): String
```
Gets the name of the audio group resource. 
get Play Mode 
```kotlin
fun getPlayMode(): AudioGroupResourcePlayMode
```
Gets the play mode of the audio group resource.