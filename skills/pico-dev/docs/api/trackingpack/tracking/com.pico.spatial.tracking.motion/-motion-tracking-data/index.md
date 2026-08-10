# MotionTrackingData | PICO Spatial SDK

tracking / com.pico.spatial.tracking.motion / MotionTrackingData 
# MotionTrackingData
```kotlin
class MotionTrackingData
```
Motion tracking data. 
Members 
## Constructors
Motion Tracking Data 
```kotlin
constructor(poses: List<MotionTrackingPose>, timestamp: Long)
```
## Properties
poses 
```kotlin
val poses: List<MotionTrackingPose>
```
The list of motion tracking poses. 
timestamp 
```kotlin
val timestamp: Long
```
UTC Time when current data is tracked in milliseconds. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get 
```kotlin
operator fun get(id: Long): MotionTrackingPose
```
Get specific motion tracker's pose. 
hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```tracker 
```kotlin
fun tracker(id: Long): MotionTrackingPose
```
Get specific motion tracker's pose.