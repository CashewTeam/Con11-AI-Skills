# translation | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / translation 
# translation
```kotlin
val translation: Vector3
```
Gets the position or translation component of this 4x4 affine transformation matrix. 
For a row-major matrix, this vector is extracted directly from the first three elements of the fourth column:  (m03, m13, m23) . These elements represent the translation (Tx, Ty, Tz) applied by the transformation. 
It assumes the matrix is an affine transformation matrix where the last row is  (0, 0, 0, 1) . 
#### Return
A  Vector3  representing the translation component of the matrix.