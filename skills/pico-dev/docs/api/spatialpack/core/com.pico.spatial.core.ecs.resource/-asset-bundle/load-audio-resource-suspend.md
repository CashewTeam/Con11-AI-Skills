# loadAudioResourceSuspend | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / loadAudioResourceSuspend 
# loadAudioResourceSuspend
```kotlin
suspend fun loadAudioResourceSuspend(path: String): AudioResource
```
Asynchronously loads an audio resource from a relative path. 
#### Return
An  AudioResource  object representing the loaded audio. 
#### Parameters
path 
The relative path to the audio resource in the  AssetBundle . 
#### Throws
Resource Loading Exception 
If any error occurs during the loading process.