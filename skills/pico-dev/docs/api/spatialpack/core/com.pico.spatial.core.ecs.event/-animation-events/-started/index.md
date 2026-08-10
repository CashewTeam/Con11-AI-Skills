# Started | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AnimationEvents / Started 
# Started
```kotlin
class Started : Event
```
This event is triggered when an animation starts, typically after calling  entity.playAnimation() . 
Members 
## Properties
playback Controller 
```kotlin
val playbackController: AnimationPlaybackController
```
The animation playback controller managing the animation that triggered the event. 
## Functions
to String 
```kotlin
open override fun toString(): String
```