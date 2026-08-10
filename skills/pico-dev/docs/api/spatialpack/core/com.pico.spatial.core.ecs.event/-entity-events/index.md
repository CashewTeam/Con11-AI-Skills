# EntityEvents | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / EntityEvents 
# EntityEvents
```kotlin
object EntityEvents
```
EntityEvents are the events which the entity invokes. 
For more information on subscribing to scene events, see  Scene.subscribe  or  com.pico.spatial.core.container.SpatialViewContent.subscribe . 
Members 
## Types
Destroy 
```kotlin
class Destroy : Event
```
Event raised when an entity is in the process of being destroyed. 
Disable 
```kotlin
class Disable : Event
```
Event raised after an entity is disabled. 
Enable 
```kotlin
class Enable : Event
```
Event raised after an entity is enabled. 
Parent Changed 
```kotlin
class ParentChanged : Event
```
Event raised when an entity changes its parent.