# subscribe | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialViewEventManager / subscribe 
# subscribe
```kotlin
@MainThread
```abstract  fun  < T  :  Event >  subscribe ( eventType :  Class < T > ,  on :  EventSource ?  =  null ,  componentType :  Class < out  Component > ?  =  null ,  subscriber :  EventSubscriber < T > ) :  Cancellable 
Subscribes to events of the specified type. 
#### Return
A cancellable object that can be used to unsubscribe from the event. 
#### Parameters
T 
The type of event to subscribe to. Must inherit from BaseEvent. 
event Type 
The class type of the event to subscribe to. 
on 
(Optional) The source of the event. If null, subscribes to all sources. 
component Type 
(Optional) The component type to filter events. If null, no component filtering is applied. 
subscriber 
The callback that handles the event when it occurs.