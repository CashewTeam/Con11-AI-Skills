# ComponentEvents | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / ComponentEvents 
# ComponentEvents
```kotlin
object ComponentEvents
```
Provides the events related to components. 
For more information on subscribing to scene events, refer to  com.pico.spatial.core.ecs.Scene.subscribe  or  com.pico.spatial.core.container.SpatialViewContent.subscribe . 
Members 
## Types
Component Added Event 
```kotlin
class ComponentAddedEvent : Event
```
This event is triggered when a component is added to an entity. 
Component Removed Event 
```kotlin
class ComponentRemovedEvent : Event
```
The event is triggered when a component is removed from an entity.