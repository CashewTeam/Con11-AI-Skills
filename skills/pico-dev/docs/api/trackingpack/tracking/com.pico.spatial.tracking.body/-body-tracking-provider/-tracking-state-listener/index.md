# TrackingStateListener | PICO Spatial SDK

tracking / com.pico.spatial.tracking.body / BodyTrackingProvider / TrackingStateListener 
# TrackingStateListener
```kotlin
fun interface TrackingStateListener
```
Listener interface for monitoring the body tracking state. 
Members 
## Functions
on State Changed 
```kotlin
abstract fun onStateChanged(state: BodyTrackingState)
```
Called when the body tracking state changes.