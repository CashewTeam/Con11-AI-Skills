# HMDPose | PICO Spatial SDK

tracking / com.pico.spatial.tracking.hmd / HMDPose 
# HMDPose
```kotlin
class HMDPose
```
The HMD position and rotation in global coordinate. 
Members 
## Constructors
HMDPose 
```kotlin
constructor(position: Vector3, rotation: Quat)
```
## Properties
position 
```kotlin
val position: Vector3
```
Position of HMD. 
rotation 
```kotlin
val rotation: Quat
```
Rotation of HMD. 
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