# loadAudioMixerGroupResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AssetBundle / loadAudioMixerGroupResource 
# loadAudioMixerGroupResource
```kotlin
fun loadAudioMixerGroupResource(path: String): AudioMixerGroupResource
```
Loads an audio mixer group resource from the specified path. 
#### Return
Returns an  AudioMixerGroupResource  object representing the loaded audio mixer group. 
#### Parameters
path 
The path to the audio mixer group resource within the  AssetBundle . 
#### Throws
Illegal State Exception 
If the asset bundle is closed. 
Resource Loading Exception 
If any error occurs during the loading process.