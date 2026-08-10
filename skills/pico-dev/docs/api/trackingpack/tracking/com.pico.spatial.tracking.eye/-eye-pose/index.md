# EyePose | PICO Spatial SDK

tracking / com.pico.spatial.tracking.eye / EyePose 
# EyePose
```kotlin
class EyePose
```
Represents the pose of eye gaze. 
Members 
## Constructors
Eye Pose 
```kotlin
constructor(position: Vector3, rotation: Quat)
```
## Properties
position 
```kotlin
val position: Vector3
```
The position of the eye gaze. 
rotation 
```kotlin
val rotation: Quat
```
The rotation of the eye gaze. 
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