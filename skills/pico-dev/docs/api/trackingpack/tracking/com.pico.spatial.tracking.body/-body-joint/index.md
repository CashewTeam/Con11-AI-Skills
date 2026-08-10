# BodyJoint | PICO Spatial SDK

tracking / com.pico.spatial.tracking.body / BodyJoint 
# BodyJoint
```kotlin
class BodyJoint
```
A body joint's position and rotation. 
Members 
## Constructors
Body Joint 
```kotlin
constructor(position: Vector3, rotation: Quat, index: BodyJoint.Index)
```
## Types
Index 
```kotlin
enum Index : Enum<BodyJoint.Index>
```
Index of body joint. 
## Properties
index 
```kotlin
val index: BodyJoint.Index
```
The index identifying the current body joint. 
position 
```kotlin
val position: Vector3
```
The position of the body joint. 
rotation 
```kotlin
val rotation: Quat
```
The rotation of the body joint. 
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