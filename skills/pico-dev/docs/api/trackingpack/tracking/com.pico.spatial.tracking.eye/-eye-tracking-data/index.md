# EyeTrackingData | PICO Spatial SDK

tracking / com.pico.spatial.tracking.eye / EyeTrackingData 
# EyeTrackingData
```kotlin
class EyeTrackingData
```
Represents eye tracking data. 
Members 
## Constructors
Eye Tracking Data 
```kotlin
constructor(eyePose: EyePose, timestamp: Long)
```
## Properties
eye Pose 
```kotlin
val eyePose: EyePose
```
Current eye pose. 
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