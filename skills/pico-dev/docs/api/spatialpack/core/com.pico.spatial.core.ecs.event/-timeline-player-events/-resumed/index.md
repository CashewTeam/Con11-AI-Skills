# Resumed | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / TimelinePlayerEvents / Resumed 
# Resumed
```kotlin
class Resumed : Event
```
This event is triggered when a timeline is resumed. This event will be triggered if you call  resume()  on a timeline player controller. 
Members 
## Properties
timeline Player Controller 
```kotlin
val timelinePlayerController: TimelinePlayerController
```
The timeline player controller managing the timeline that triggers this event. 
## Functions
to String 
```kotlin
open override fun toString(): String
```