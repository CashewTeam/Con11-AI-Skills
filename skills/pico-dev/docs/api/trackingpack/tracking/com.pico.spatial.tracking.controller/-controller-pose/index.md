# ControllerPose | PICO Spatial SDK

tracking / com.pico.spatial.tracking.controller / ControllerPose 
# ControllerPose
```kotlin
class ControllerPose
```
A controller's position and rotation in global coordinate. 
Members 
## Constructors
Controller Pose 
```kotlin
constructor(position: Vector3, rotation: Quat)
```
## Properties
position 
```kotlin
val position: Vector3
```
Position of controller. 
rotation 
```kotlin
val rotation: Quat
```
Rotation of controller. 
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