# TrackerRequestCompleteListener | PICO Spatial SDK

tracking / com.pico.spatial.tracking.motion / MotionTrackingProvider / TrackerRequestCompleteListener 
# TrackerRequestCompleteListener
```kotlin
fun interface TrackerRequestCompleteListener
```
Listener for receiving completion events when tracker pairing is done. 
Members 
## Functions
on Request Complete 
```kotlin
abstract fun onRequestComplete(trackerIdCollection: MotionTrackerIdCollection)
```
Called when tracker pairing is completed and the user returns to your application.