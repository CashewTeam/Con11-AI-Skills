# PlaybackCompleted | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AudioEvents / PlaybackCompleted 
# PlaybackCompleted
```kotlin
class PlaybackCompleted : Event
```
This event is triggered when an audio completes playback without any interruption. 
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