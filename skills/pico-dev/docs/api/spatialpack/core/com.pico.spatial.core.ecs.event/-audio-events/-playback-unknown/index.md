# PlaybackUnknown | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AudioEvents / PlaybackUnknown 
# PlaybackUnknown
```kotlin
class PlaybackUnknown : Event
```
This event is triggered when an error occurs during the current playback, including a decoding error, an I/O error, and more. 
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