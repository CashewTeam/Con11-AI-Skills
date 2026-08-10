# AudioStreamPlayerController | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamPlayerController 
# AudioStreamPlayerController
```kotlin
class AudioStreamPlayerController : Closeable
```
Central controller for managing PCM audio stream playback. 
This class provides granular control over audio stream operations including playback state management, real-time audio data injection, and playback parameter adjustments. It serves as the primary interface between application logic and the underlying audio system. 
Note: This controller only supports playback of PCM audio streams. Therefore, when using  writeStreamData  to write or  AudioStreamDataCallback  to send audio stream data, only raw PCM audio data is accepted. Any audio file format headers must be removed before writing or sending the audio stream data—for example, skip the first 44 bytes of a WAV file header. 
This controller provides two modes of data delivery: 
- 
Push mode: Data is written directly to the audio stream buffer using  writeStreamData . 
- 
Pull mode: Data is provided by an external source, such as an audio file, using      AudioStreamDataCallback . 
In push mode, the application writes audio data directly to the audio stream buffer using  writeStreamData . The controller will then play the audio data from the buffer. 
In pull mode, the application provides an  AudioStreamDataCallback  to the controller via  Entity.playAudioStream  and  Entity.prepareAudioStream , which will produce the callback to require more audio data. The controller will then play the audio data from the callback. 
When to use null callback: 
- 
In push mode: Caller manages data flow via  AudioStreamPlayerController.writeStreamData . 
- 
When audio data will be provided through direct buffer writes. 
- 
For static or pre-loaded audio content. 
When to provide callback: 
- 
In pull mode: System requests data on-demand through  AudioStreamDataCallback.onMoreData . 
- 
For dynamic/streaming audio content. 
- 
When implementing real-time audio processing. 
Key capabilities: 
- 
Full lifecycle control (play/pause/stop/resume) 
- 
Precision timing via nanosecond timestamps 
- 
Dynamic playback speed adjustment 
- 
Volume fading with multiple interpolation modes 
- 
Dual-mode data delivery (push/pull) 
- 
Thread-safe main-thread enforcement 
Usage scenarios: 
- 
Real-time audio streaming applications 
- 
Interactive audio environments 
- 
Synchronized multimedia playback 
- 
Dynamic audio effect systems 
Example: Basic playback control 

```
val controller = entity.playAudioStream(config)controller.play()controller.setVolume(0.8f)controller.fade(targetVolume = 0.0f, duration = 2000L) // Fade out over 2 seconds
```
Example: Push mode data writing 

```
val pushConfig = AudioStreamConfig(    AudioChannelLayoutType.STANDARD,    "mix_group_1",    AudioChannelLayout.OUTPUT_LAYOUT_STEREO,    AmbisonicsType.NONE,    AudioFormat(sampleRate = 48000),    null)val controller = entity.prepareAudioStream(pushConfig)// Calculate the delay time and buffer sizeval delayTime = 120val channelCnt = pushConfig.audioChannelCountval audioFormat = pushConfig.audioFormat!!val audioTrackBufferFrameCnt = (audioFormat.sampleRate / 1000) * delayTimeval frameSize = audioFormat.getFrameSize(channelCnt)val audioTrackBufferSize = audioTrackBufferFrameCnt * frameSizeval mappedBuffer = ByteBuffer.allocateDirect(audioTrackBufferSize)// Prepare to write audio data in IO thread with coroutineCoroutineScope(Dispatchers.IO).launch {    var remainSize = mappedBuffer.remaining()    while (remainSize > 0) {        // wait for controller playing        if (controller.isPlaying() != true) {            delay(30)            continue        }        remainSize = mappedBuffer.remaining()        val chunkSize = min(audioTrackBufferSize, remainSize)        val sliceBuffer = mappedBuffer.slice().limit(chunkSize) as ByteBuffer        val actualFrames = chunkSize / frameSize        val writeResult = controller.writeStreamData(sliceBuffer, actualFrames, false)        if (writeResult == actualFrames.toLong()) {            mappedBuffer.position(mappedBuffer.position() + chunkSize)            val bufferDurationMs = (actualFrames * 1000L) / audioFormat.sampleRate            delay(bufferDurationMs)        } else if (writeResult > 0 && writeResult < actualFrames.toLong()) {            mappedBuffer.position(mappedBuffer.position() + (writeResult * frameSize).toInt())            val bufferDurationMs = (writeResult * 1000L) / audioFormat.sampleRate            delay(bufferDurationMs)        } else {             // Log.w("PcmStreamHelper", "writeStreamData failed writeResult: $writeResult")             delay(20)        }    } } // Start audio stream playback controller.play() // Release audio stream resource when no longer needed controller.stop() controller.close() mappedBuffer.clear() pushConfig.close()
```
Example: Timestamp synchronization 

```
val timestamp = controller.getStreamTimestamp()videoPlayer.syncWithAudio(timestamp.timeNs)
```
#### See also
Audio Stream Config 
For configuration of audio stream parameters 
Audio Interpolator Type 
For available fade interpolation algorithms 
Members 
## Properties
entity 
```kotlin
val entity: Entity?
```
The entity that the audio is playing on. 
valid 
```kotlin
@get:JvmName(name = "isValid")
```val  valid :  Boolean 
The controller is valid. 
## Functions
close 
```kotlin
open override fun close()
```fade 
```kotlin
fun fade(targetVolume: Float = 1.0f, duration: Long, fadeMode: AudioInterpolatorType = AudioInterpolatorType.CUBIC): Boolean
```
Fade the audio to the specified volume over a specified duration. 
flush Stream 
```kotlin
fun flushStream(): Boolean
```
Flush the audio stream to discard any remaining data in player buffer. 
get Playback Speed 
```kotlin
fun getPlaybackSpeed(): Float
```
Get the audio playback speed. 
get Stream Position 
```kotlin
fun getStreamPosition(): Long
```
Retrieves the current stream position in bytes. 
get Stream Timestamp 
```kotlin
@ExperimentalSpatialApi
```fun  getStreamTimestamp ( ) :  AudioStreamTimestamp ? 
Retrieves high-precision playback timing information. 
get Volume 
```kotlin
fun getVolume(): Float
```
Gets the playback volume. 
is Playing 
```kotlin
fun isPlaying(): Boolean
```
Check audio is playing or not. 
pause 
```kotlin
fun pause(): Boolean
```
Pause the playing state audio. 
play 
```kotlin
fun play(): Boolean
```
Play audio. 
resume 
```kotlin
fun resume(): Boolean
```
Resume the pausing state audio. 
set Playback Speed 
```kotlin
fun setPlaybackSpeed(rate: Float): Boolean
```
Set the audio playback speed. 
set Volume 
```kotlin
fun setVolume(@FloatRange(from = 0.0, to = 1.0) volume: Float = 1.0f): Boolean
```
Sets the playback volume. 
stop 
```kotlin
fun stop(): Boolean
```
Stop audio. 
write Stream Data 
```kotlin
@Synchronized
```fun  writeStreamData ( buffer :  ByteBuffer ,  frameCount :  Int ,  blocking :  Boolean ) :  Long 
Writes pcm audio data in push mode operation, which is suitable for real-time audio,the buffer must be direct buffer and the owner of the buffer must be the caller, and the buffer must be released after no longer needed.