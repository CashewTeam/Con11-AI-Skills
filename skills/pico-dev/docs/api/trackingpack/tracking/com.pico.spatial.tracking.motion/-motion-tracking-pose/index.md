# MotionTrackingPose | PICO Spatial SDK

tracking / com.pico.spatial.tracking.motion / MotionTrackingPose 
# MotionTrackingPose
```kotlin
class MotionTrackingPose
```
A motion tracker's position and rotation. 
Members 
## Constructors
Motion Tracking Pose 
```kotlin
constructor(id: Long, position: Vector3, rotation: Quat)
```
## Properties
id 
```kotlin
val id: Long
```
The id of the motion tracker. 
position 
```kotlin
val position: Vector3
```
Position of motion tracker. 
rotation 
```kotlin
val rotation: Quat
```
Rotation of motion tracker. 
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