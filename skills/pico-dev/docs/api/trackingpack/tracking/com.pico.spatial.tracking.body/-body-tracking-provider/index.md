# BodyTrackingProvider | PICO Spatial SDK

tracking / com.pico.spatial.tracking.body / BodyTrackingProvider 
# BodyTrackingProvider
```kotlin
@RequiredFullSpace
```object  BodyTrackingProvider  :  DataProvider < BodyTrackingData >  
Provides body tracking data. For usage details, refer to  DataProvider . 
Starting the body tracking provider on an uncalibrated device will fail. You can call  start  with  BodyTrackingStartInfo  to launch the PICO Motion Tracker app to calibrate body tracking. 
Body tracking data contains 24 body joints, each joint has 6DoF pose data. You can get the full pose data by  BodyTrackingData.bodyPose  and the pose of each joint by  BodyPose.bodyJoints . 

```
bodyTrackingData.bodyPose.bodyJoints.forEach {    // Get the rotation and position of each joint    it.rotation    it.position    // Identify joint by index    it.index}
```
You can register a  TrackingStateListener  using  addTrackingStateListener  to receive updates on the body tracking state. 
#### See also
Data Provider Body Tracking Data Members 
## Types
Tracking State Listener 
```kotlin
fun interface TrackingStateListener
```
Listener interface for monitoring the body tracking state. 
## Functions
add Tracking State Listener 
```kotlin
fun addTrackingStateListener(callback: BodyTrackingProvider.TrackingStateListener)
```
Adds the  TrackingStateListener  to receive body tracking state. 
remove Tracking State Listener 
```kotlin
fun removeTrackingStateListener(callback: BodyTrackingProvider.TrackingStateListener)
```
Removes the  TrackingStateListener  to stop receiving body tracking state. 
start 
```kotlin
fun start(startInfo: BodyTrackingStartInfo): DataProvider.StartResult
```
Starts providing body tracking data using the specified  BodyTrackingStartInfo .