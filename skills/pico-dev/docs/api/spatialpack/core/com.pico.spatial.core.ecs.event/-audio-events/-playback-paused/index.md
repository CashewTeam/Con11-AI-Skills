# PlaybackPaused | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AudioEvents / PlaybackPaused 
# PlaybackPaused
```kotlin
class PlaybackPaused : Event
```
This event is triggered when a playing audio is paused by calling  controller.pause() . 
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