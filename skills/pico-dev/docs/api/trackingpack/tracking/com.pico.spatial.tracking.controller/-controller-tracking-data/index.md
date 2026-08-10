# ControllerTrackingData | PICO Spatial SDK

tracking / com.pico.spatial.tracking.controller / ControllerTrackingData 
# ControllerTrackingData
```kotlin
@RequiredFullSpace
```class  ControllerTrackingData 
Controllers' tracking data. 
Members 
## Constructors
Controller Tracking Data 
```kotlin
constructor(left: ControllerPose?, right: ControllerPose?, timestamp: Long)
```
## Properties
left 
```kotlin
val left: ControllerPose?
```
Left controller pose. 
right 
```kotlin
val right: ControllerPose?
```
Right controller pose. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```