# inverse | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / inverse 
# inverse
```kotlin
fun inverse(): Matrix4
```
Calculates and returns the inverse of this 4x4 matrix. 
This method computes the inverse using the adjugate matrix method, which involves calculating the determinant and the adjugate (transpose of the cofactor matrix) of this matrix. The inverse is then calculated as  (1/determinant) * adjugate . 
#### Return
A new  Matrix4  instance that is the inverse of this matrix. 
#### Throws
Illegal Argument Exception 
If the matrix is singular (i.e., its determinant is zero), and therefore cannot be inverted.