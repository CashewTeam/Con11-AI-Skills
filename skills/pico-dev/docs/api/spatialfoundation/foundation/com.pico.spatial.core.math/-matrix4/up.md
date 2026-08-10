# up | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / up 
# up
```kotlin
val up: Vector3
```
Gets the basis vector representing the Y-axis of the coordinate system after this matrix's transformation. This is commonly referred to as the "up" vector. 
For a row-major matrix, this vector is extracted directly from the first three elements of the second row:  (m10, m11, m12) . 
If the matrix includes scaling, this vector's length will reflect that scaling, and it is not guaranteed to be a unit vector. To get a pure direction, normalize this vector. 
#### Return
A  Vector3  representing the transformed Y-axis, including any scaling.