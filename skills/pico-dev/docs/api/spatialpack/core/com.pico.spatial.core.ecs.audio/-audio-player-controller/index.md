# AudioPlayerController | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioPlayerController 
# AudioPlayerController
```kotlin
class AudioPlayerController : Closeable
```
A handle that is used to control audio playback，including playing, pausing, resuming, stopping an audio, and checking the playback status of an audio. 
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
get Current Position 
```kotlin
fun getCurrentPosition(): Long
```
Gets the current playback position of the audio file in milliseconds. 
get Duration 
```kotlin
fun getDuration(): Long
```
Gets the total duration of the audio file in milliseconds. 
get Playback Speed 
```kotlin
fun getPlaybackSpeed(): Float
```
Gets the current playback speed for the audio. 
get Volume 
```kotlin
fun getVolume(): Float
```
Gets the playback volume. 
is Completed 
```kotlin
fun isCompleted(): Boolean
```
Checks if an audio is finished playing or not. 
is Playing 
```kotlin
fun isPlaying(): Boolean
```
Checks if an audio is playing or not. 
pause 
```kotlin
fun pause(): Boolean
```
Pauses an audio that is playing. 
play 
```kotlin
fun play(): Boolean
```
Plays an audio. 
resume 
```kotlin
fun resume(): Boolean
```
Resumes a paused audio. 
seek To 
```kotlin
fun seekTo(position: Long): Boolean
```
Seeks to the specified playback position in the current audio. 
set Loop 
```kotlin
fun setLoop(loop: Boolean): Boolean
```
Enables or disables looping for audio playback. 
set Playback Speed 
```kotlin
fun setPlaybackSpeed(rate: Float): Boolean
```
Sets the playback speed for the audio. 
set Volume 
```kotlin
fun setVolume(@FloatRange(from = 0.0, to = 1.0) volume: Float = 1.0f): Boolean
```
Set the playback volume. 
stop 
```kotlin
fun stop(): Boolean
```
Stops an audio.