# ComponentAddedEvent | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / ComponentEvents / ComponentAddedEvent 
# ComponentAddedEvent
```kotlin
class ComponentAddedEvent : Event
```
This event is triggered when a component is added to an entity. 
Members 
## Properties
component Type 
```kotlin
val componentType: Class<out Component>
```
The type of component that is added. 
entity 
```kotlin
val entity: Entity
```
The entity that the component is added to. 
## Functions
to String 
```kotlin
open override fun toString(): String
```