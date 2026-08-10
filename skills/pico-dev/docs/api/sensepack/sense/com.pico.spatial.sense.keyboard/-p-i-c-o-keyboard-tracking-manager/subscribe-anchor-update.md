# subscribeAnchorUpdate | PICO Spatial SDK

sense / com.pico.spatial.sense.keyboard / PICOKeyboardTrackingManager / subscribeAnchorUpdate 
# subscribeAnchorUpdate
```kotlin
fun subscribeAnchorUpdate(subscriber: AnchorUpdateSubscriber<PICOKeyboardAnchor>): Cancellable
```
Subscribes to keyboard anchor update events. 
The supplied  subscriber  receives incremental updates whenever a keyboard anchor is added, updated, removed, or reported as loaded by the system. Use the returned  Cancellable  to end the subscription when updates are no longer needed. 
Subscribing before calling  start  is recommended when callers want to observe the earliest possible updates after the tracking manager begins running. 
#### Return
A  Cancellable  that unregisters this subscriber. 
#### Parameters
subscriber 
The callback that receives  AnchorUpdate  events for  PICOKeyboardAnchor s.