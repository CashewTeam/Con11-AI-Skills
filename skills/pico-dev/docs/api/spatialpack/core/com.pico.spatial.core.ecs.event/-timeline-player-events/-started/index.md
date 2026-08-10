# Started | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / TimelinePlayerEvents / Started 
# Started
```kotlin
class Started : Event
```
This event is triggered when a timeline starts, typically after calling  entity.playTimeline() . 
Members 
## Properties
timeline Player Controller 
```kotlin
val timelinePlayerController: TimelinePlayerController
```
The timeline player controller managing the timeline that triggered the event. 
## Functions
to String 
```kotlin
open override fun toString(): String
```