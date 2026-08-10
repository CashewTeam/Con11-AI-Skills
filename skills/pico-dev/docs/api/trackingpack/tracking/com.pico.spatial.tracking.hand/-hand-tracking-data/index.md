# HandTrackingData | PICO Spatial SDK

tracking / com.pico.spatial.tracking.hand / HandTrackingData 
# HandTrackingData
```kotlin
@RequiredFullSpace
```class  HandTrackingData 
Represents the hand tracking data. 
Members 
## Constructors
Hand Tracking Data 
```kotlin
constructor(left: HandPose?, right: HandPose?, timestamp: Long)
```
## Properties
left 
```kotlin
val left: HandPose?
```
The pose of the left hand. 
right 
```kotlin
val right: HandPose?
```
The pose of the right hand. 
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