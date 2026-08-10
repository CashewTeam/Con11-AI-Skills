# ComponentRemovedEvent | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / ComponentEvents / ComponentRemovedEvent 
# ComponentRemovedEvent
```kotlin
class ComponentRemovedEvent : Event
```
The event is triggered when a component is removed from an entity. 
Members 
## Properties
component Type 
```kotlin
val componentType: Class<out Component>
```
The type of component that is removed. 
entity 
```kotlin
val entity: Entity
```
The entity that the component is removed from. 
## Functions
to String 
```kotlin
open override fun toString(): String
```