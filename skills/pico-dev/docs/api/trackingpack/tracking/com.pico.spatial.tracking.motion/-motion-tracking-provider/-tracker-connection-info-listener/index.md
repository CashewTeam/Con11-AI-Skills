# TrackerConnectionInfoListener | PICO Spatial SDK

tracking / com.pico.spatial.tracking.motion / MotionTrackingProvider / TrackerConnectionInfoListener 
# TrackerConnectionInfoListener
```kotlin
fun interface TrackerConnectionInfoListener
```
Listener for receiving connection information updates from motion trackers. 
Members 
## Functions
on Connection Info Update 
```kotlin
abstract fun onConnectionInfoUpdate(connectionInfo: MotionTrackerConnectionInfo)
```
Called when a motion tracker is connected or disconnected.