# TrackerBatteryInfoListener | PICO Spatial SDK

tracking / com.pico.spatial.tracking.motion / MotionTrackingProvider / TrackerBatteryInfoListener 
# TrackerBatteryInfoListener
```kotlin
fun interface TrackerBatteryInfoListener
```
Listener for receiving battery information updates from motion trackers. 
Members 
## Functions
on Battery Info Update 
```kotlin
abstract fun onBatteryInfoUpdate(batteryInfo: MotionTrackerBatteryInfo)
```
Called when the battery info of a motion tracker is updated.