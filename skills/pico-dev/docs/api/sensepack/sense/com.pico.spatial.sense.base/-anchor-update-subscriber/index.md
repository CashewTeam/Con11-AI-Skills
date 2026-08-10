# AnchorUpdateSubscriber | PICO Spatial SDK

sense / com.pico.spatial.sense.base / AnchorUpdateSubscriber 
# AnchorUpdateSubscriber
```kotlin
fun interface AnchorUpdateSubscriber<T : Anchor>
```
AnchorUpdateSubscriber is a subscriber for anchor update events. 
Members 
## Functions
on Update 
```kotlin
abstract fun onUpdate(anchorUpdate: AnchorUpdate<T>)
```
Called when an anchor update event is received.