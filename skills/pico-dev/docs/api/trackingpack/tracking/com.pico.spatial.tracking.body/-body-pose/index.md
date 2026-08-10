# BodyPose | PICO Spatial SDK

tracking / com.pico.spatial.tracking.body / BodyPose 
# BodyPose
```kotlin
class BodyPose
```
A body pose, includes 24 joints. 
Members 
## Constructors
Body Pose 
```kotlin
constructor(bodyJoints: List<BodyJoint>)
```
## Properties
body Joints 
```kotlin
val bodyJoints: List<BodyJoint>
```
List of all body joints. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get 
```kotlin
operator fun get(index: BodyJoint.Index): BodyJoint
```
Get specific joint. 
hash Code 
```kotlin
open override fun hashCode(): Int
```joint 
```kotlin
fun joint(index: BodyJoint.Index): BodyJoint
```
Get specific joint. 
to String 
```kotlin
open override fun toString(): String
```