# subscribeAnchorUpdate | PICO Spatial SDK

sense / com.pico.spatial.sense.world / WorldTrackingManager / subscribeAnchorUpdate 
# subscribeAnchorUpdate
```kotlin
fun subscribeAnchorUpdate(subscriber: AnchorUpdateSubscriber<WorldAnchor>): Cancellable
```
Subscribes to anchor update events. 
#### Return
The  Cancellable  object that can be used to cancel the subscription. 
#### Parameters
subscriber 
The subscriber object.