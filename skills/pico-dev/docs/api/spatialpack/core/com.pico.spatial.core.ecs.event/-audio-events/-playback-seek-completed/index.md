# PlaybackSeekCompleted | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AudioEvents / PlaybackSeekCompleted 
# PlaybackSeekCompleted
```kotlin
class PlaybackSeekCompleted : Event
```
This event is triggered when a seek operation completes via  controller.seekTo()  in the current playback. 
Members 
## Properties
playback Controller 
```kotlin
val playbackController: AudioPlayerController
```
The audio playback controller managing the audio that triggers this event. 
## Functions
to String 
```kotlin
open override fun toString(): String
```