# Destroy | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / EntityEvents / Destroy 
# Destroy
```kotlin
class Destroy : Event
```
Event raised when an entity is in the process of being destroyed. 
This event is triggered before the destruction of the entity, allowing listeners to perform any necessary cleanup or operations related to the entity's lifecycle. 
Members 
## Properties
entity 
```kotlin
val entity: Entity?
```
The entity that is being destroyed. 
## Functions
to String 
```kotlin
open override fun toString(): String
```