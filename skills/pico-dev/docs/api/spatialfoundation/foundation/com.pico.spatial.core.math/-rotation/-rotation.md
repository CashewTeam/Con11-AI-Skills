# Rotation | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Rotation / Rotation 
# Rotation
```kotlin
constructor(quat: Quat)
```
#### Parameters
quat 
The initial quaternion to create the rotation from. It does not need to be a unit quaternion, as it will be normalized internally. 
```kotlin
constructor(eulerAngles: EulerAngles)
```
Creates a  Rotation  from Euler angles specified in a  EulerAngles  object. Assumes  EulerAngles  angles (pitch, yaw, roll) are in  degrees  and correspond to a specific Euler rotation sequence (e.g., intrinsic ZYX for roll, new Y for yaw, newest X for pitch) handled by  EulerAngles.toQuat() . 
#### Parameters
euler Angles 
A  EulerAngles  object containing pitch, yaw, and roll in degrees. 
```kotlin
constructor(angle: Float, axis: Vector3)
```
Creates a  Rotation  from an angle (in  radians ) and an axis of rotation. The axis vector will be normalized if it's not already a unit vector by the Quat constructor. 
#### Parameters
angle 
The rotation angle in  radians . 
axis 
The axis of rotation (Vector3). Should be a non-zero vector.