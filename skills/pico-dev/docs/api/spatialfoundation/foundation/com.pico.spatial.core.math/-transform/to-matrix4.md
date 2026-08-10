# toMatrix4 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Transform / toMatrix4 
# toMatrix4
```kotlin
fun toMatrix4(): Matrix4
```
Reconstructs a 4x4 transformation matrix from this Transform's position, quaternion, and scale components. 
The final transformation is equivalent to applying scale, then rotation, and finally translation. The matrix multiplication order is therefore M = M_translation * M_rotation * M_scale. 
This implementation directly computes the final matrix elements without intermediate matrix allocations. 
#### Return
The combined 4x4 transformation  Matrix4 .