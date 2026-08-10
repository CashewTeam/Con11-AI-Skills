# com.pico.spatial.core.ecs.event | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event 
# Package-level declarations
Types 
## Types
Animation Events 
```kotlin
object AnimationEvents
```
Provides events triggered when the entity plays animations. 
Audio Events 
```kotlin
object AudioEvents
```
Provides events triggered when the entity plays an audio resource. 
Collision Events 
```kotlin
object CollisionEvents
```
Provides events triggered when collisions occur between entities. 
Component Events 
```kotlin
object ComponentEvents
```
Provides the events related to components. 
Entity Events 
```kotlin
object EntityEvents
```
EntityEvents are the events which the entity invokes. 
Event 
```kotlin
sealed class Event
```
The base type of event. 
Event Subscriber 
```kotlin
fun interface EventSubscriber<T : Event>
```
A function that subscribes to an event. 
Scene Events 
```kotlin
object SceneEvents
```
SceneEvents are the events which the scene invokes. 
Timeline Player Events 
```kotlin
object TimelinePlayerEvents
```
Provides events triggered when the timeline player controller is updated.