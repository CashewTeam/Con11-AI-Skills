# AudioGroupResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioGroupResource / AudioGroupResource 
# AudioGroupResource
```kotlin
constructor(name: String, audioResources: List<AudioResource>, mode: AudioGroupResourcePlayMode = AudioGroupResourcePlayMode.FORWARD)
```
Creates an AudioGroupResource from a list of AudioResources. 
This constructor creates a new audio group resource that contains a collection of audio resources. The group can play the audio resources in different orders based on the specified  mode . 
#### Parameters
name 
The name for the audio group resource. This name is used to identify the group in the resource system. 
audio Resources 
The list of  AudioResource  objects to group together. 
mode 
The  AudioGroupResourcePlayMode  that defines the playback order for the audio group. Defaults to  AudioGroupResourcePlayMode.FORWARD . 
#### Throws
Resource Loading Exception 
If any error occurs during creating. 
Illegal Argument Exception 
if any parameter is invalid.