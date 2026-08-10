# loadAudioResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / loadAudioResource 
# loadAudioResource
```kotlin
fun loadAudioResource(path: String): AudioResource
```
Loads an audio resource from a relative path. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage it may cause jank or even ANR. 
- 
Prefer the async API  loadAudioResourceSuspend(...) . If you must use a sync call, execute it off the main thread or in a coroutine context such as  withContext(Dispatchers.IO) . 
#### Return
An  AudioResource  object representing the loaded audio. 
#### Parameters
path 
The relative path to the audio resource in the  AssetBundle . 
#### Throws
Resource Loading Exception 
If any error occurs during the loading process.