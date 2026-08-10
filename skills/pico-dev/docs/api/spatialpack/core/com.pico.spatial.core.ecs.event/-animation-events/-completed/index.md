# Completed | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AnimationEvents / Completed 
# Completed
```kotlin
class Completed : Event
```
This event is triggered when an animation completes naturally. This event will not be triggered if you call  stop()  on a playback controller. 
Members 
## Properties
playback Controller 
```kotlin
val playbackController: AnimationPlaybackController
```
The animation playback controller managing the animation that triggers this event. 
## Functions
to String 
```kotlin
open override fun toString(): String
```