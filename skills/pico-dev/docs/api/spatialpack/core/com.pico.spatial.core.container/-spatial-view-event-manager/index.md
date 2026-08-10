# SpatialViewEventManager | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialViewEventManager 
# SpatialViewEventManager
```kotlin
interface SpatialViewEventManager
```
Provides event subscription for a  SpatialView 's content. 
#### Inheritors
SpatialViewContent Members 
## Functions
subscribe 
```kotlin
@MainThread
```abstract  fun  < T  :  Event >  subscribe ( eventType :  Class < T > ,  on :  EventSource ?  =  null ,  componentType :  Class < out  Component > ?  =  null ,  subscriber :  EventSubscriber < T > ) :  Cancellable 
Subscribes to events of the specified type.