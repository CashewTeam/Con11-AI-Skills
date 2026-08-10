# SceneEvents | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / SceneEvents 
# SceneEvents
```kotlin
object SceneEvents
```
SceneEvents are the events which the scene invokes. 
For more information on subscribing to scene events, see  Scene.subscribe  or  com.pico.spatial.core.container.SpatialViewContent.subscribe . 
Members 
## Types
Entity Added 
```kotlin
class EntityAdded : Event
```
Event raised after an entity is added to the scene. 
Entity Remove 
```kotlin
class EntityRemove : Event
```
Event raised when an entity is in the process of being removed from its current scene. 
Update 
```kotlin
class Update : Event
```
Event raised after the scene is updated.