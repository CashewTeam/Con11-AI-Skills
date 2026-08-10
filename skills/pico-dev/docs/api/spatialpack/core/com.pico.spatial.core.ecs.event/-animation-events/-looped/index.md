# Looped | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AnimationEvents / Looped 
# Looped
```kotlin
class Looped : Event
```
If the animation is set to loop upon creation, this event is triggered each time the animation completes a loop. 
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