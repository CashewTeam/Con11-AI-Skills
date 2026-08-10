# com.pico.spatial.tracking.hand | PICO Spatial SDK

tracking / com.pico.spatial.tracking.hand 
# Package-level declarations
Types 
## Types
Hand Joint 
```kotlin
class HandJoint
```
Represents a single hand joint, including its position and rotation. 
Hand Pose 
```kotlin
class HandPose
```
Represents the pose of a hand, including 26 hand joints. 
Hand Tracking Data 
```kotlin
@RequiredFullSpace
```class  HandTrackingData 
Represents the hand tracking data. 
Hand Tracking Provider 
```kotlin
@RequiredFullSpace
```class  HandTrackingProvider  :  DataProvider < HandTrackingData >  
Provides hand tracking data. For usage details, refer to  DataProvider .