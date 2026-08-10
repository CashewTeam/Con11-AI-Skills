# Rotation | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Rotation 
# Rotation
```kotlin
class Rotation(quat: Quat)
```
Represents a rotation in three-dimensional space. 
This class uses an internal unit quaternion ( Quat ) for robust and unambiguous representation of rotations, avoiding issues like gimbal lock inherent in Euler angles for complex interpolations. 
It provides constructors from various representations like Euler angles ( EulerAngles ), axis-angle, and quaternions. Properties allow accessing the rotation as a quaternion, axis-angle (angle in radians), or converting to Euler angles. Operations include composition, inversion, and spherical linear interpolation (Slerp). 
#### Parameters
quat 
The initial quaternion to create the rotation from. It does not need to be a unit quaternion, as it will be normalized internally. 
Members 
## Constructors
Rotation 
```kotlin
constructor(quat: Quat)
```
```kotlin
constructor(eulerAngles: EulerAngles)
```
Creates a  Rotation  from Euler angles specified in a  EulerAngles  object. Assumes  EulerAngles  angles (pitch, yaw, roll) are in  degrees  and correspond to a specific Euler rotation sequence (e.g., intrinsic ZYX for roll, new Y for yaw, newest X for pitch) handled by  EulerAngles.toQuat() . 
```kotlin
constructor(angle: Float, axis: Vector3)
```
Creates a  Rotation  from an angle (in  radians ) and an axis of rotation. The axis vector will be normalized if it's not already a unit vector by the Quat constructor. 
## Types
Companion 
```kotlin
object Companion
```
Companion object providing utilities for rotation operations. 
## Properties
angle 
```kotlin
val angle: Float
```
The angle of rotation in  degrees , in the range  [0, 180] . 
axis 
```kotlin
val axis: Vector3
```
The normalized axis of rotation. For an identity rotation (zero angle), a default axis (e.g., Z-axis) may be returned. 
euler Angles 
```kotlin
val eulerAngles: EulerAngles
```
Gets the euler angle representation of this rotation as a  EulerAngles  object. 
inverse 
```kotlin
val inverse: Rotation
```
The inverse of this rotation. For a unit quaternion, this is its conjugate. 
is Identity 
```kotlin
val isIdentity: Boolean
```
A boolean value that indicates whether this rotation is effectively an identity rotation (no rotation). Checks if the scalar part  w  of the internal quaternion is close to +/-1 and the vector part  (x,y,z)  is close to zero, within  EPSILON(1e-6f)  and  EPSILON_SQ(1e-12f)  tolerances. 
quaternion 
```kotlin
val quaternion: Quat
```
The internal unit quaternion that represents this rotation. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```times 
```kotlin
operator fun times(other: Rotation): Rotation
```
Combines this rotation with another rotation  other . The result  this * other  represents applying the rotation  other  first, then applying  this  rotation. The resulting quaternion is normalized to counteract potential floating-point drift. 
to String 
```kotlin
open override fun toString(): String
```