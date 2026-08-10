# MotionTrackingProvider | PICO Spatial SDK

tracking / com.pico.spatial.tracking.motion / MotionTrackingProvider 
# MotionTrackingProvider
```kotlin
@RequiredFullSpace
```object  MotionTrackingProvider  :  DataProvider < MotionTrackingData >  
Provides motion tracking data. For usage details, refer to  DataProvider . 
You can request a specific number of motion trackers using  start  with  MotionTrackingStartInfo , and receive the result via  addRequestCompleteListener . Below is a code sample: 

```
val startInfo = MotionTrackingStartInfo.Builder().apply {    // Request two motion trackers    requestDeviceCount = 2}.build()MotionTrackingProvider.addRequestCompleteListener(MotionTrackingProvider.TrackerRequestCompleteListener {    // Get tracker IDs    it.ids    // Check if the number of trackers is enough    if (it.ids.size < 2) {        // May notice the user and request again    } else {        // Save the IDs for use after the callback    }})MotionTrackingProvider.start(startInfo)
```
Motion tracking data contains a list of tracker poses. Each tracker has 6DoF data. You can get all poses via  MotionTrackingData.poses  or get the pose of a specific tracker by ID using  MotionTrackingData.get . Below is a code sample: 

```
// 'ids' is obtained from the request complete listenerids.forEach {    // Get each tracker's pose    val pose = motionTrackingData[it]    pose.position    pose.rotation}
```
#### See also
Data Provider Motion Tracking Data Members 
## Types
Tracker Battery Info Listener 
```kotlin
fun interface TrackerBatteryInfoListener
```
Listener for receiving battery information updates from motion trackers. 
Tracker Connection Info Listener 
```kotlin
fun interface TrackerConnectionInfoListener
```
Listener for receiving connection information updates from motion trackers. 
Tracker Key Event Listener 
```kotlin
fun interface TrackerKeyEventListener
```
Listener for receiving key events from motion trackers. 
Tracker Request Complete Listener 
```kotlin
fun interface TrackerRequestCompleteListener
```
Listener for receiving completion events when tracker pairing is done. 
## Functions
add Battery Info Listener 
```kotlin
fun addBatteryInfoListener(listener: MotionTrackingProvider.TrackerBatteryInfoListener)
```
Adds the  TrackerBatteryInfoListener  to receive the battery information of the motion tracker. 
add Connection Info Listener 
```kotlin
fun addConnectionInfoListener(listener: MotionTrackingProvider.TrackerConnectionInfoListener)
```
Adds the  TrackerConnectionInfoListener  to receive the connection information of the motion tracker. 
add Key Event Listener 
```kotlin
fun addKeyEventListener(listener: MotionTrackingProvider.TrackerKeyEventListener)
```
Adds the  TrackerKeyEventListener  to receive key events from the motion tracker. 
add Request Complete Listener 
```kotlin
fun addRequestCompleteListener(listener: MotionTrackingProvider.TrackerRequestCompleteListener)
```
Adds the  TrackerRequestCompleteListener  to receive notifications when a tracker request completes. 
remove Battery Info Listener 
```kotlin
fun removeBatteryInfoListener(listener: MotionTrackingProvider.TrackerBatteryInfoListener)
```
Removes the  TrackerBatteryInfoListener  to stop receiving the battery information of the motion tracker. 
remove Connection Info Listener 
```kotlin
fun removeConnectionInfoListener(listener: MotionTrackingProvider.TrackerConnectionInfoListener)
```
Removes the  TrackerConnectionInfoListener  to stop receiving the connection information of the motion tracker. 
remove Key Event Listener 
```kotlin
fun removeKeyEventListener(listener: MotionTrackingProvider.TrackerKeyEventListener)
```
Removes the  TrackerKeyEventListener  to stop receiving key events from the motion tracker. 
remove Request Complete Listener 
```kotlin
fun removeRequestCompleteListener(listener: MotionTrackingProvider.TrackerRequestCompleteListener)
```
Removes the  TrackerRequestCompleteListener  to stop receiving notifications about tracker request completion. 
start 
```kotlin
fun start(startInfo: MotionTrackingStartInfo): DataProvider.StartResult
```
Starts providing motion tracking data using the specified  MotionTrackingStartInfo .