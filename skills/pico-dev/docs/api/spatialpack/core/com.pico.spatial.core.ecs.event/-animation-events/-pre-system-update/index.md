# PreSystemUpdate | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / AnimationEvents / PreSystemUpdate 
# PreSystemUpdate
```kotlin
class PreSystemUpdate : Event
```
This event is triggered immediately before the animation system starts updating for a frame. 
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