# Paused | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / TimelinePlayerEvents / Paused 
# Paused
```kotlin
class Paused : Event
```
This event is triggered when a timeline is paused. This event will be triggered if you call  pause()  on a timeline player controller. 
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