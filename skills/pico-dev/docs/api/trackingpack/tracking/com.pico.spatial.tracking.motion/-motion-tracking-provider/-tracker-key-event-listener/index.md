# TrackerKeyEventListener | PICO Spatial SDK

tracking / com.pico.spatial.tracking.motion / MotionTrackingProvider / TrackerKeyEventListener 
# TrackerKeyEventListener
```kotlin
fun interface TrackerKeyEventListener
```
Listener for receiving key events from motion trackers. 
Members 
## Functions
on Key Event 
```kotlin
abstract fun onKeyEvent(keyEvent: MotionTrackerKeyEvent)
```
Called when a key on the motion tracker is pressed.