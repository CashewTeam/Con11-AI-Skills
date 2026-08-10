# AudioResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioResource 
# AudioResource
```kotlin
class AudioResource : AudioAsset
```
The  Resource  type for audio. 
Members 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  AudioResource . 
## Functions
close 
```kotlin
open override fun close()
```
You need to manually release the resource to free the memory it occupies. 
get Config 
```kotlin
fun getConfig(): AudioResourceConfig
```
Gets the configuration of the audio resource. 
get Name 
```kotlin
fun getName(): String
```
Gets the name of the audio resource.