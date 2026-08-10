# PostSystemUpdate | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AnimationEvents / PostSystemUpdate 
# PostSystemUpdate
```kotlin
class PostSystemUpdate : Event
```
This event is triggered immediately after the animation system finishes updating for a frame. 
Members 
## Properties
delta Time 
```kotlin
val deltaTime: Float
```
The elapsed time since the previous animation system update. 
## Functions
to String 
```kotlin
open override fun toString(): String
```