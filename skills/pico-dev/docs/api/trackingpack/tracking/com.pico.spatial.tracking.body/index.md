# com.pico.spatial.tracking.body | PICO Spatial SDK

tracking / com.pico.spatial.tracking.body 
# Package-level declarations
Types 
## Types
Body Joint 
```kotlin
class BodyJoint
```
A body joint's position and rotation. 
Body Pose 
```kotlin
class BodyPose
```
A body pose, includes 24 joints. 
Body Tracking Data 
```kotlin
class BodyTrackingData
```
Body tracking data. 
Body Tracking Message 
```kotlin
enum BodyTrackingMessage : Enum<BodyTrackingMessage>
```
Message of body tracking. 
Body Tracking Provider 
```kotlin
@RequiredFullSpace
```object  BodyTrackingProvider  :  DataProvider < BodyTrackingData >  
Provides body tracking data. For usage details, refer to  DataProvider . 
Body Tracking Start Info 
```kotlin
class BodyTrackingStartInfo
```
Configuration used to start  BodyTrackingProvider . 
Body Tracking State 
```kotlin
class BodyTrackingState
```
State of body tracking. 
Body Tracking Status 
```kotlin
enum BodyTrackingStatus : Enum<BodyTrackingStatus>
```
Status of body tracking.