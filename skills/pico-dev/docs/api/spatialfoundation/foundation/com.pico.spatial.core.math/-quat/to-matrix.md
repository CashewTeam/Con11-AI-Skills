# toMatrix | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / toMatrix 
# toMatrix
```kotlin
fun toMatrix(): Matrix4
```
Converts this quaternion into an equivalent 4x4 rotation matrix. 
The quaternion is first normalized internally to ensure that the resulting matrix represents a pure rotation (without any scaling). If this quaternion has a near-zero length, it cannot represent a valid rotation, and an identity matrix is returned as a safe fallback. 
The conversion uses the standard mathematical formula to create a 3x3 rotation matrix from the components of the unit quaternion  (x, y, z, w) . This 3x3 matrix is then embedded in the top-left of the final 4x4 matrix. 
The resulting matrix is suitable for post-multiplying column vectors (e.g.,  TransformedPoint = RotationMatrix * OriginalPoint ). 
#### Return
A  Matrix4  representing the rotation. Returns an identity matrix if this quaternion has a length close to zero.