# Paused | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AnimationEvents / Paused 
# Paused
```kotlin
class Paused : Event
```
This event is triggered when a playing animation is paused by calling  controller.pause() . 
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