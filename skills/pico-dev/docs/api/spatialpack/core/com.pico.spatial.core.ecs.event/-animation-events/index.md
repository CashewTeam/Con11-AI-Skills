# AnimationEvents | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AnimationEvents 
# AnimationEvents
```kotlin
object AnimationEvents
```
Provides events triggered when the entity plays animations. 
For more information on subscribing to scene events, refer to  com.pico.spatial.core.ecs.Scene.subscribe  or  com.pico.spatial.core.container.SpatialViewContent.subscribe . 
Members 
## Types
Completed 
```kotlin
class Completed : Event
```
This event is triggered when an animation completes naturally. This event will not be triggered if you call  stop()  on a playback controller. 
Looped 
```kotlin
class Looped : Event
```
If the animation is set to loop upon creation, this event is triggered each time the animation completes a loop. 
Paused 
```kotlin
class Paused : Event
```
This event is triggered when a playing animation is paused by calling  controller.pause() . 
Post System Update 
```kotlin
class PostSystemUpdate : Event
```
This event is triggered immediately after the animation system finishes updating for a frame. 
Pre System Update 
```kotlin
class PreSystemUpdate : Event
```
This event is triggered immediately before the animation system starts updating for a frame. 
Resumed 
```kotlin
class Resumed : Event
```
This event is triggered when a paused animation is resumed by calling  controller.resume() . 
Started 
```kotlin
class Started : Event
```
This event is triggered when an animation starts, typically after calling  entity.playAnimation() . 
Terminated 
```kotlin
class Terminated : Event
```
This event is triggered when an animation is explicitly stopped by calling  controller.stop() , regardless of whether it is completed.