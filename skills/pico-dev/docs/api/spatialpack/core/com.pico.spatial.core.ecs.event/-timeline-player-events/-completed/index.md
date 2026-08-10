# Completed | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / TimelinePlayerEvents / Completed 
# Completed
```kotlin
class Completed : Event
```
This event is triggered when a timeline completes naturally. This event will not be triggered if you call  stop()  on a timeline player controller. 
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