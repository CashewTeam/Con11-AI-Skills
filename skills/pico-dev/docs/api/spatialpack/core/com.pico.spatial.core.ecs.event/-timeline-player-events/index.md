# TimelinePlayerEvents | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / TimelinePlayerEvents 
# TimelinePlayerEvents
```kotlin
object TimelinePlayerEvents
```
Provides events triggered when the timeline player controller is updated. 
For more information on subscribing to scene events, refer to  com.pico.spatial.core.ecs.Scene.subscribe  or  com.pico.spatial.core.container.SpatialViewContent.subscribe . 
Members 
## Types
Completed 
```kotlin
class Completed : Event
```
This event is triggered when a timeline completes naturally. This event will not be triggered if you call  stop()  on a timeline player controller. 
Paused 
```kotlin
class Paused : Event
```
This event is triggered when a timeline is paused. This event will be triggered if you call  pause()  on a timeline player controller. 
Resumed 
```kotlin
class Resumed : Event
```
This event is triggered when a timeline is resumed. This event will be triggered if you call  resume()  on a timeline player controller. 
Started 
```kotlin
class Started : Event
```
This event is triggered when a timeline starts, typically after calling  entity.playTimeline() . 
Terminated 
```kotlin
class Terminated : Event
```
This event is triggered when a timeline is terminated. This event will be triggered if you call  stop()  on a timeline player controller.