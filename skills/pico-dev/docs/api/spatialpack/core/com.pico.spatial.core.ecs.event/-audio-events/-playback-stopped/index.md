# PlaybackStopped | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AudioEvents / PlaybackStopped 
# PlaybackStopped
```kotlin
class PlaybackStopped : Event
```
This event is triggered when a playing audio is stopped by calling  controller.stop() . 
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