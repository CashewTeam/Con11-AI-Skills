# Terminated | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AnimationEvents / Terminated 
# Terminated
```kotlin
class Terminated : Event
```
This event is triggered when an animation is explicitly stopped by calling  controller.stop() , regardless of whether it is completed. 
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