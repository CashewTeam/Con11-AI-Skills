# HandTrackingProvider | PICO Spatial SDK

tracking / com.pico.spatial.tracking.hand / HandTrackingProvider 
# HandTrackingProvider
```kotlin
@RequiredFullSpace
```class  HandTrackingProvider  :  DataProvider < HandTrackingData >  
Provides hand tracking data. For usage details, refer to  DataProvider . 
Hand tracking data includes the poses of both left and right hands. Each hand contains 26 joints, and each joint has 6DoF pose data. You can get the pose of each hand via  HandTrackingData.left  and  HandTrackingData.right , and get the pose of each joint via  HandPose.handJoints . 

```
// Get the pose of the left handhandTrackingData.left?.handJoints.forEach {    // Get the rotation and position of each joint    it.rotation    it.position    // Identify a joint by index    it.index}
```
#### See also
Data Provider Hand Tracking Data Members 
## Constructors
Hand Tracking Provider 
```kotlin
constructor()
```