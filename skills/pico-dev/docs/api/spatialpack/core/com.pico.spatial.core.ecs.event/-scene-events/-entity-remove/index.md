# EntityRemove | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / SceneEvents / EntityRemove 
# EntityRemove
```kotlin
class EntityRemove : Event
```
Event raised when an entity is in the process of being removed from its current scene. 
This event is triggered as part of the removal process of an entity from its current scene. It allows listeners to perform cleanup or respond to the removal of the entity. Note that this event is specific to the scene and will not propagate to other scenes. 
Members 
## Properties
entity 
```kotlin
val entity: Entity?
```
The entity being removed from the scene. 
## Functions
to String 
```kotlin
open override fun toString(): String
```