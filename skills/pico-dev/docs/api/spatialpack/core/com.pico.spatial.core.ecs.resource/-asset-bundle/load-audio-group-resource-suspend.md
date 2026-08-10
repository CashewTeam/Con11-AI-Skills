# loadAudioGroupResourceSuspend | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / loadAudioGroupResourceSuspend 
# loadAudioGroupResourceSuspend
```kotlin
suspend fun loadAudioGroupResourceSuspend(path: String): AudioGroupResource
```
Asynchronously loads an audio group resource from the specified path. 
#### Return
Returns an  AudioGroupResource  object representing the loaded audio group. 
#### Parameters
path 
The path to the audio group resource within the  AssetBundle . 
#### Throws
Illegal State Exception 
If the asset bundle is closed. 
Resource Loading Exception 
If any error occurs during the loading process.