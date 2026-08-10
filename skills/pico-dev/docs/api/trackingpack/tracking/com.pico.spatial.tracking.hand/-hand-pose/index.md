# HandPose | PICO Spatial SDK

tracking / com.pico.spatial.tracking.hand / HandPose 
# HandPose
```kotlin
class HandPose
```
Represents the pose of a hand, including 26 hand joints. 
Members 
## Constructors
Hand Pose 
```kotlin
constructor(handJoints: List<HandJoint>)
```
## Properties
hand Joints 
```kotlin
val handJoints: List<HandJoint>
```
A list of all hand joints. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```get 
```kotlin
operator fun get(index: HandJoint.Index): HandJoint
```
Gets a specific joint. 
hash Code 
```kotlin
open override fun hashCode(): Int
```joint 
```kotlin
fun joint(index: HandJoint.Index): HandJoint
```
Gets a specific joint. 
to String 
```kotlin
open override fun toString(): String
```