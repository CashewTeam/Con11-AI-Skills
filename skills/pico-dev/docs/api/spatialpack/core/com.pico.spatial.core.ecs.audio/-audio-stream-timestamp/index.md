# AudioStreamTimestamp | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioStreamTimestamp 
# AudioStreamTimestamp
```kotlin
class AudioStreamTimestamp
```
Represents precise timing information for audio stream playback. 
This class provides two key metrics for audio synchronization and monitoring: 
- 
Frame-based position tracking 
- 
High-resolution timestamping 
Typical use cases include: 
- 
Audio/video synchronization 
- 
Playback progress monitoring 
- 
Latency measurement 
- 
Real-time audio processing 
Usage example: 

```
val timestamp = audioController.getStreamTimestamp()println("Current frame: ${timestamp.framePosition} at ${timestamp.timeNs} nanoseconds")// Calculate time since playback startedval elapsedSeconds = (timestamp.timeNs - startTimeNs) / 1e9
```Members 
## Properties
frame Position 
```kotlin
val framePosition: Long
```
The frame position of current audio data being played by controller in audio stream. 
time Ns 
```kotlin
val timeNs: Long
```
The timestamp of current audio frame data being played by controller, precision is nanoseconds.