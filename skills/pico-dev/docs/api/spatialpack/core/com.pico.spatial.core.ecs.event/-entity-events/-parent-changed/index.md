# ParentChanged | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / EntityEvents / ParentChanged 
# ParentChanged
```kotlin
class ParentChanged : Event
```
Event raised when an entity changes its parent. 
This event is triggered when an entity's parent is updated. If the entity moves from one scene to another, the event will be raised in the new scene. In such cases, the  previousParent  will be  null , indicating the entity has no parent in the previous scene or the parent is no longer valid. 
Members 
## Properties
entity 
```kotlin
val entity: Entity?
```
The entity whose parent has changed. 
previous Parent 
```kotlin
val previousParent: Entity?
```
The previous parent of the entity. This will be  null  if the entity has moved to a different scene or no valid previous parent exists. 
## Functions
to String 
```kotlin
open override fun toString(): String
```