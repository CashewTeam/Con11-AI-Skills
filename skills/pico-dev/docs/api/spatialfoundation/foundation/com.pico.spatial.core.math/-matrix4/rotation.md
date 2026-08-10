# rotation | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / rotation 
# rotation
```kotlin
val rotation: Quat
```
Extracts the pure rotational component of this 4x4 matrix as a  Quat  (quaternion). 
This getter first isolates the rotational basis by normalizing the first three row vectors ( right ,  up ,  forward ) of the matrix, effectively removing any scaling. It then converts the resulting pure 3x3 rotation matrix into a unit quaternion using a numerically stable algorithm that avoids issues with large rotation angles. 
This operation discards any translation and scaling information from the original matrix. If the matrix contains shear, the resulting rotation is the best-fit orthogonal approximation. 
#### Return
A unit  Quat  representing the pure rotation of this matrix.