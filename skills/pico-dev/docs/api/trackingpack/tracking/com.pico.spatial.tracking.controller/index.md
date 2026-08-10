# com.pico.spatial.tracking.controller | PICO Spatial SDK

tracking / com.pico.spatial.tracking.controller 
# Package-level declarations
Types 
## Types
Controller Action 
```kotlin
class ControllerAction
```
Snapshot of input actions for a single controller. 
Controller Action Data 
```kotlin
@RequiredFullSpace
```class  ControllerActionData 
Input actions for both left and right controllers. 
Controller Pose 
```kotlin
class ControllerPose
```
A controller's position and rotation in global coordinate. 
Controller Tracking Data 
```kotlin
@RequiredFullSpace
```class  ControllerTrackingData 
Controllers' tracking data. 
Controller Tracking Provider 
```kotlin
@RequiredFullSpace
```class  ControllerTrackingProvider  :  DataProvider < ControllerTrackingData >  
Provider for controller tracking data and action callbacks; see  DataProvider . 
Thumbstick Value 
```kotlin
class ThumbstickValue
```
2D value for a controller thumbstick.