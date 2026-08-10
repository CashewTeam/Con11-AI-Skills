# AudioStreamBufferData | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamBufferData 
# AudioStreamBufferData
```kotlin
class AudioStreamBufferData
```
Container for streaming audio data buffers provided during  AudioStreamDataCallback  execution. 
This class supplies a  buffer  indicating where to write audio stream data when the callback is invoked. The  frameCount  and  frameSize  properties specify how much data can be written into the buffer. 
## Ownership & Lifecycle
- 
Owner : The audio engine — it allocates and destroys instances. 
- 
Allocation : Managed internally by the audio engine. 
- 
Lifetime : Valid only during the callback execution. 
## Usage Example

```
object pullCallback : AudioStreamDataCallback {    override fun onMoreData(buffer: AudioStreamBufferData) {        val byteArray = ByteArray(bufferSize.toInt())        val readSize = audioStream.read(byteArray)        buffer.put(byteArray)        if (readSize < bufferSize) {            val remainingBytes = bufferSize - readSize            buffer.put(ByteArray(remainingBytes.toInt()) { 0 })        }        buffer.flip()    }}
```
## Thread Safety
- 
Access only within the callback thread context. 
- 
Not thread-safe for concurrent usage. 
Members 
## Properties
buffer 
```kotlin
val buffer: ByteBuffer
```
Direct memory buffer. 
frame Count 
```kotlin
val frameCount: Long
```
Number of audio frames to process. 
frame Size 
```kotlin
val frameSize: Long
```
Memory size of individual frame.