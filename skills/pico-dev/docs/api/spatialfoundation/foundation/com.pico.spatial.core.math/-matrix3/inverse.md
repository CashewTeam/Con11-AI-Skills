# inverse | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix3 / inverse 
# inverse
```kotlin
fun inverse(): Matrix3
```
Calculates the inverse of this 3x3 matrix. 
The inverse is computed using the adjugate matrix method divided by the determinant:  A⁻¹ = adj(A) / det(A) . 
This function includes a check to ensure the matrix is numerically invertible. It verifies that the absolute value of the determinant is greater than  1e-6f . If the determinant is too close to zero, indicating the matrix is singular or ill-conditioned, an  IllegalArgumentException  is thrown. 
#### Return
A new  Matrix3  instance representing the inverse of this matrix. 
#### Throws
Illegal Argument Exception 
if the absolute value of the determinant is less than or equal to  1e-6f , meaning the matrix cannot be reliably inverted.