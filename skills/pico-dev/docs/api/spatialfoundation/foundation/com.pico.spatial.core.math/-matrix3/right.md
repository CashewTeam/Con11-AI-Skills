# right | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix3 / right 
# right
```kotlin
val right: Vector3
```
Gets the basis vector representing the X-axis of the coordinate system after this matrix's transformation. This is commonly referred to as the "right" vector. 
For a row-major matrix, this vector is extracted directly from the first row:  (m00, m01, m02) . 
If the matrix includes scaling, this vector's length will reflect that scaling and it is not guaranteed to be a unit vector. 
#### Return
A  Vector3  representing the transformed X-axis.