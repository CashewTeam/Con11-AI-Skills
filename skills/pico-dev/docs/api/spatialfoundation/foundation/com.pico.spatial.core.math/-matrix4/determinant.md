# determinant | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / determinant 
# determinant
```kotlin
fun determinant(): Float
```
Calculates the determinant of this 4x4 matrix. 
The determinant is a scalar value that provides important information about the matrix, such as whether it is invertible and how it scales volume/hyper - volume. A non-zero determinant indicates an invertible matrix. The sign of the determinant indicates whether the transformation preserves or reverses orientation (handedness). 
This implementation uses the full Leibniz formula to calculate the determinant of the 4x4 matrix. Note that direct expansion for 4x4 determinants can be verbose and potentially susceptible to loss of precision for ill - conditioned matrices, though it is a standard algebraic method. 
#### Return
The determinant of the matrix as a  Float .