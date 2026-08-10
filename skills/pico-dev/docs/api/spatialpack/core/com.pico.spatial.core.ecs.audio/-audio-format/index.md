# AudioFormat | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioFormat 
# AudioFormat
```kotlin
class AudioFormat
```
Represents audio format configuration for spatial audio processing. 
This class encapsulates the complete specification for audio data format, including: 
- 
Data type of audio samples (e.g., 16-bit integer, 32-bit float). 
- 
Sampling rate (default: 48000 Hz). 
- 
Channel data layout (interleaved/non-interleaved). 
- 
Byte ordering (little-endian/big-endian). 
Typical usage scenarios: 
- 
Audio capture configuration: 

```
val format = AudioFormat( channelDataType =    AudioFormat.AudioChannelDataType.INT16, sampleRate = 44100 )
```
- 
Format validation and comparison: 
```
if (inputFormat == expectedFormat) { // Handle compatible format }
```Members 
## Constructors
Audio Format 
```kotlin
constructor(channelDataType: AudioFormat.AudioChannelDataType = AudioChannelDataType.INT16, sampleRate: Int = 48000, interleaved: Boolean = true, littleEndian: Boolean = true)
```
Constructs audio format with detailed parameters. 
## Types
Audio Channel Data Type 
```kotlin
enum AudioChannelDataType : Enum<AudioFormat.AudioChannelDataType>
```
The AudioChannelDataType audio type, which can be either signed 8-bit, signed 16-bit, signed 24-bit, signed 32-bit, or 32-bit floating point. 
## Properties
channel Data Type 
```kotlin
var channelDataType: AudioFormat.AudioChannelDataType
```
The audio channel data type, which can be either signed 8-bit, signed 16-bit, signed 24-bit, signed 32-bit, or 32-bit floating point. 
interleaved 
```kotlin
var interleaved: Boolean
```
Whether the channel data is interleaved, default is true. 
little Endian 
```kotlin
var littleEndian: Boolean
```
Whether the channel data is little endian, default is true. 
sample Rate 
```kotlin
var sampleRate: Int
```
The sample rate of the channel data, default is 48000. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get Frame Size 
```kotlin
fun getFrameSize(channelCnt: Int): Int
```
Get the size of a frame in bytes. 
hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```