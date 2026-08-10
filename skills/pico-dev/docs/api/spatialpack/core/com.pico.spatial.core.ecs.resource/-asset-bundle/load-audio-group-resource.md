# loadAudioGroupResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / loadAudioGroupResource 
# loadAudioGroupResource
```kotlin
fun loadAudioGroupResource(path: String): AudioGroupResource
```
Loads an audio group resource from the specified path. 
WARNING: 
- 
This method performs blocking I/O. While it can be called on the main thread, on slow devices or with unstable storage it may cause jank or even ANR. 
- 
Prefer the async API  loadAudioGroupResourceSuspend(...) . If you must use a sync call, execute it off the main thread or in a coroutine context such as  withContext(Dispatchers.IO) . 
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