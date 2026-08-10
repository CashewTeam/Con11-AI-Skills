# AudioStreamDataCallback | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamDataCallback 
# AudioStreamDataCallback
```kotlin
interface AudioStreamDataCallback
```
Callback interface for providing audio stream data in pull mode. 
Implement this interface to receive audio data requests from the system. 
Members 
## Functions
on More Data 
```kotlin
abstract fun onMoreData(bufferData: AudioStreamBufferData)
```
Called by the system to request audio data.