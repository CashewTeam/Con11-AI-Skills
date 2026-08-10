# EventSubscriber | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / EventSubscriber 
# EventSubscriber
```kotlin
fun interface EventSubscriber<T : Event>
```
A function that subscribes to an event. 
#### Parameters
T 
The type of the event. 
Members 
## Functions
on Event 
```kotlin
abstract fun onEvent(event: T)
```
Called when an event is received.