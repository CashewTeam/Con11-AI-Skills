# HandJoint | PICO Spatial SDK

tracking / com.pico.spatial.tracking.hand / HandJoint 
# HandJoint
```kotlin
class HandJoint
```
Represents a single hand joint, including its position and rotation. 
Members 
## Constructors
Hand Joint 
```kotlin
constructor(position: Vector3, rotation: Quat, index: HandJoint.Index)
```
## Types
Index 
```kotlin
enum Index : Enum<HandJoint.Index>
```
Represents the indices of hand joints. 
## Properties
index 
```kotlin
val index: HandJoint.Index
```
The index identifying the current hand joint. 
position 
```kotlin
val position: Vector3
```
The position of the hand joint. 
rotation 
```kotlin
val rotation: Quat
```
The rotation of the hand joint. 
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