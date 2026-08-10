# playAudioStream | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / playAudioStream 
# playAudioStream
```kotlin
@MainThread
```fun  playAudioStream ( config :  AudioStreamConfig ,  callback :  AudioStreamDataCallback ?  =  null ) :  AudioStreamPlayerController 
Immediately starts playing an audio stream with the specified configuration. 
This method initializes audio resources and begins playback in a single operation. Typical use cases: 
- 
Low-latency audio streaming requiring immediate playback. 
- 
Push-mode audio where data is provided through  AudioStreamPlayerController.writeStreamData . 
Example with pull mode: 

```
val config = AudioStreamConfig(    AudioChannelLayoutType.AMBISONICS,    "mix_group_2",    AudioChannelLayout.OUTPUT_LAYOUT_INVALID,    AmbisonicsType.ACN_SN3D_1,    AudioFormat(sampleRate = 96000))val pullCallback =  object : AudioStreamDataCallback {     override fun onMoreData(bufferData: AudioStreamBufferData) {         // Provide audio data to the stream,write your processing logic here.     } }val controller = entity.prepareAudioStream(config,pullCallback)controller.play()// Release audio stream resource when no longer neededcontroller.stop()controller.close()config.close()
```
Example with push mode: 

```
val config = AudioStreamConfig(    AudioChannelLayoutType.STANDARD,    "mix_group_1",    AudioChannelLayout.OUTPUT_LAYOUT_STEREO,    AmbisonicsType.NONE,    AudioFormat(sampleRate = 48000))val controller = entity.prepareAudioStream(config)// Calculate the delay time and buffer sizeval delayTime = 120val channelCnt = config.audioChannelCountval audioFormat = config.audioFormat!!val audioTrackBufferFrameCnt = (audioFormat.sampleRate / 1000) * delayTimeval frameSize = audioFormat.getFrameSize(channelCnt)val audioTrackBufferSize = audioTrackBufferFrameCnt * frameSizeval mappedBuffer = ByteBuffer.allocateDirect(audioTrackBufferSize)// Prepare to write audio data in IO thread with coroutineCoroutineScope(Dispatchers.IO).launch {    var remainSize = mappedBuffer.remaining()    while (remainSize > 0) {        // wait for controller playing        if (controller.isPlaying() != true) {            delay(30)            continue        }        remainSize = mappedBuffer.remaining()        val chunkSize = min(audioTrackBufferSize, remainSize)        val sliceBuffer = mappedBuffer.slice().limit(chunkSize) as ByteBuffer        val actualFrames = chunkSize / frameSize        val writeResult = controller.writeStreamData(sliceBuffer, actualFrames, false)        if (writeResult == actualFrames.toLong()) {            mappedBuffer.position(mappedBuffer.position() + chunkSize)            val bufferDurationMs = (actualFrames * 1000L) / audioFormat.sampleRate            delay(bufferDurationMs)        } else if (writeResult > 0 && writeResult < actualFrames.toLong()) {            mappedBuffer.position(mappedBuffer.position() + (writeResult * frameSize).toInt())            val bufferDurationMs = (writeResult * 1000L) / audioFormat.sampleRate            delay(bufferDurationMs)        } else {            delay(20)        }    } } // Release audio stream resource when no longer needed controller.stop() controller.close() mappedBuffer.clear()
```
#### Return
Controller for managing active audio stream. Check  AudioStreamPlayerController.valid  before interaction. 
#### Parameters
config 
Configuration for the audio stream, including:     - Audio format specifications.     - Channel layout type (Standard or Ambisonics).     - Mix group settings.     - Once the stream starts, the configuration becomes immutable.     - After calling this method, the config is bound to an AudioStreamPlayerController.       Modifications are not allowed, and reuse with other AudioStreamPlayerController       instances is prohibited, especially if the originally bound       AudioStreamPlayerController.close is no longer valid. 
callback 
Callback for providing audio data when using pull mode.     - Required when using pull mode.     - Called on a background thread.     - Implement  AudioStreamDataCallback.onMoreData  to provide audio data.     - Callback is invoked when system requests more data.     - The callback can be null when using push mode, where data is provided directly       through  AudioStreamPlayerController.writeStreamData . 
Note: 
- 
Callback is not required for push mode. 
- 
Data is provided directly through  AudioStreamPlayerController.writeStreamData . 
When to use null callback: 
- 
In push mode: Caller manages data flow via  AudioStreamPlayerController.writeStreamData . 
- 
When audio data will be provided through direct buffer writes. 
- 
For static or preloaded audio content. 
When to provide callback: 
- 
In pull mode: System requests data on-demand through  AudioStreamDataCallback.onMoreData . 
- 
For dynamic/streaming audio content. 
- 
When implementing real-time audio processing. 
#### See also
Audio Stream Player Controller 
For real-time data writing and playback monitoring. 
Audio Stream Config 
For configuration requirements. 
#### Throws
Illegal State Exception 
If: 
- 
Called off main thread. 
- 
Configuration validation fails ( AudioStreamConfig.valid  == false). 
- 
Entity lacks required audio component.