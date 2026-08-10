# Resumed | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AnimationEvents / Resumed 
# Resumed
```kotlin
class Resumed : Event
```
This event is triggered when a paused animation is resumed by calling  controller.resume() . 
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