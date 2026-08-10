# BodyTrackingData | PICO Spatial SDK

tracking / com.pico.spatial.tracking.body / BodyTrackingData 
# BodyTrackingData
```kotlin
class BodyTrackingData
```
Body tracking data. 
Members 
## Constructors
Body Tracking Data 
```kotlin
constructor(bodyPose: BodyPose, timestamp: Long)
```
## Properties
body Pose 
```kotlin
val bodyPose: BodyPose
```
Current body pose. 
timestamp 
```kotlin
val timestamp: Long
```
UTC Time when current data is tracked in milliseconds. 
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