# PlaybackStarted | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AudioEvents / PlaybackStarted 
# PlaybackStarted
```kotlin
class PlaybackStarted : Event
```
This event is triggered when an audio starts playing, typically after calling  entity.playAudio() . 
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