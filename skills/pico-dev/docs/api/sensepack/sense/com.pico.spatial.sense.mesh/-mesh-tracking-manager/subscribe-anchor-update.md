# subscribeAnchorUpdate | PICO Spatial SDK

sense / com.pico.spatial.sense.mesh / MeshTrackingManager / subscribeAnchorUpdate 
# subscribeAnchorUpdate
```kotlin
fun subscribeAnchorUpdate(subscriber: AnchorUpdateSubscriber<MeshAnchor>): Cancellable
```
Subscribes to anchor update events. 
This function allows developers to register a callback to receive notifications whenever a mesh anchor is added, updated, or removed. The subscription can be canceled using the returned  Cancellable  object. 
#### Return
A  Cancellable  object that can be used to cancel the subscription. 
#### Parameters
subscriber 
The subscriber object that will handle anchor update events.