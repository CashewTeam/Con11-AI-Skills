# EulerAngles | PICO Spatial SDK

foundation / com.pico.spatial.core.math / EulerAngles 
# EulerAngles
```kotlin
class EulerAngles(val pitch: Float = 0.0f, val yaw: Float = 0.0f, val roll: Float = 0.0f)
```
Represents a rotation in 3D space using euler angles. 
The  EulerAngles  class defines a rotation by three angles: pitch, yaw, and roll. To avoid ambiguity, the rotation is applied as a specific  extrinsic ZXY sequence . This means the rotations are performed in order around fixed world axes: 
- 
First, a  Roll  is applied around the  world Z-axis . 
- 
Second, a  Pitch  is applied around the  world X-axis . 
- 
Finally, a  Yaw  is applied around the  world Y-axis . 
The combined transformation matrix that transforms a point  p  is a result of the multiplication order  M = M_yaw_Y * M_pitch_X * M_roll_Z , so  p_new = M * p . This extrinsic ZXY sequence is also equivalent to an  intrinsic YXZ  rotation (applying Yaw, then Pitch, then Roll around the object's own moving axes). 
All rotation angles are provided and stored in  degrees . 
Members 
## Constructors
Euler Angles 
```kotlin
constructor(pitch: Float = 0.0f, yaw: Float = 0.0f, roll: Float = 0.0f)
```
## Types
Companion 
```kotlin
object Companion
```
Provides utilities for angle conversion between degrees and radians. 
## Properties
pitch 
```kotlin
val pitch: Float
```
The pitch angle (for the rotation around the X-axis) in degrees. 
roll 
```kotlin
val roll: Float
```
The roll angle (for the rotation around the Z-axis) in degrees. 
yaw 
```kotlin
val yaw: Float
```
The yaw angle (for the rotation around the Y-axis) in degrees. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```equivalent Check 
```kotlin
fun equivalentCheck(other: EulerAngles): Boolean
```
Determines whether two rotation operations are equivalent. 
hash Code 
```kotlin
open override fun hashCode(): Int
```is Finite 
```kotlin
fun isFinite(): Boolean
```
Checks if the  EulerAngles  instance is valid. 
to Quat 
```kotlin
fun toQuat(): Quat
```
Converts this  EulerAngles  instance into its equivalent  Quat  (quaternion) representation. 
to String 
```kotlin
open override fun toString(): String
```