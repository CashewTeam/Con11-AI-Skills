# toAngleAxis | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / toAngleAxis 
# toAngleAxis
```kotlin
fun toAngleAxis(): Pair<Float, Vector3>
```
Converts this quaternion to its equivalent angle-axis representation, with the angle returned in  degrees . 
The quaternion is first normalized internally. If the quaternion has a near-zero length (norm squared < 1e-12f), it's treated as an identity rotation, returning an angle of  0.0  degrees and a default Z-axis  (0,0,1) . 
For non-zero quaternions, the conversion ensures that the scalar part ( w ) of the normalized quaternion used for internal radian angle calculation is non-negative. This results in the radian angle being in  [0, PI] , which is then converted to degrees, yielding an angle in the range  [0, 180]  degrees. 
If the calculated rotation angle is very close to zero (specifically, if  sin(radian_angle/2)  is less than  1e-6f ), an angle of  0.0  degrees and a default Z-axis are returned. 
#### Return
A  Pair<Float, Vector3> , where: 
- 
first  (Float): The rotation angle in  degrees , in the range  [0, 180] . 
- 
second  (Vector3): The normalized axis of rotation. For a zero rotation angle, a default axis (e.g., Z-axis  (0,0,1) ) is returned.