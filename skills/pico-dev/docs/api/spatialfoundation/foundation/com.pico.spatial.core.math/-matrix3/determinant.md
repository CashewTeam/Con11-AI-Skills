# determinant | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix3 / determinant 
# determinant
```kotlin
fun determinant(): Float
```
Calculates the determinant of this 3x3 matrix. 
The determinant is a scalar value that can be used to determine if the matrix is invertible (it's invertible if and only if the determinant is non-zero). It also represents the volume scaling factor of the linear transformation described by the matrix (or area scaling in 2D, sign indicates orientation change). 
#### Return
The determinant of the matrix as a  Float .