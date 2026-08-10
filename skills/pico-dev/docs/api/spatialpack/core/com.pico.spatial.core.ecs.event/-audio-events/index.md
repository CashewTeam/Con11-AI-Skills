# AudioEvents | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AudioEvents 
# AudioEvents
```kotlin
object AudioEvents
```
Provides events triggered when the entity plays an audio resource. 
For more information on subscribing to scene events, refer to  com.pico.spatial.core.ecs.Scene.subscribe  or  com.pico.spatial.core.container.SpatialViewContent.subscribe . 
Members 
## Types
Playback Completed 
```kotlin
class PlaybackCompleted : Event
```
This event is triggered when an audio completes playback without any interruption. 
Playback Paused 
```kotlin
class PlaybackPaused : Event
```
This event is triggered when a playing audio is paused by calling  controller.pause() . 
Playback Seek Completed 
```kotlin
class PlaybackSeekCompleted : Event
```
This event is triggered when a seek operation completes via  controller.seekTo()  in the current playback. 
Playback Started 
```kotlin
class PlaybackStarted : Event
```
This event is triggered when an audio starts playing, typically after calling  entity.playAudio() . 
Playback Stopped 
```kotlin
class PlaybackStopped : Event
```
This event is triggered when a playing audio is stopped by calling  controller.stop() . 
Playback Unknown 
```kotlin
class PlaybackUnknown : Event
```
This event is triggered when an error occurs during the current playback, including a decoding error, an I/O error, and more.