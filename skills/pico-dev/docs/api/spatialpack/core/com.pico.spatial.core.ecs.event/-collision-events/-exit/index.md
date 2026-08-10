# Exit | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / CollisionEvents / Exit 
# Exit
```kotlin
class Exit : Event
```
This event is triggered when two objects that are in contact separate. 
Members 
## Properties
entity A 
```kotlin
val entityA: Entity?
```
The first entity involved in the collision. 
entity B 
```kotlin
val entityB: Entity?
```
The second entity involved in the collision. 
## Functions
to String 
```kotlin
open override fun toString(): String
```