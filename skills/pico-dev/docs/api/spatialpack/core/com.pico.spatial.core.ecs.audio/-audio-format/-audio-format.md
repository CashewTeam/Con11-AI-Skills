# AudioFormat | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioFormat / AudioFormat 
# AudioFormat
```kotlin
constructor(channelDataType: AudioFormat.AudioChannelDataType = AudioChannelDataType.INT16, sampleRate: Int = 48000, interleaved: Boolean = true, littleEndian: Boolean = true)
```
Constructs audio format with detailed parameters. 
#### Parameters
channel Data Type 
Sample data type (default: INT16 - most common format). 
sample Rate 
Sampling frequency in Hz (default: 48000 - professional audio standard). 
interleaved 
Storage layout (default: true - interleaved format for most use cases). 
little Endian 
Byte order (default: true - little-endian for x86/ARM architectures).