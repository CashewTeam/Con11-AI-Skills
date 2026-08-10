# getPlayMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioGroupResource / getPlayMode 
# getPlayMode
```kotlin
fun getPlayMode(): AudioGroupResourcePlayMode
```
Gets the play mode of the audio group resource. 
This method returns the play mode that was specified when this audio group resource was created. The play mode determines the playback order for audio resources within the group. 
#### Return
The  AudioGroupResourcePlayMode  of the audio group resource. 
#### Throws
Illegal State Exception 
If this resource has been closed or is invalid.