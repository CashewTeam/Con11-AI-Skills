# forward | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / forward 
# forward
```kotlin
val forward: Vector3
```
Gets the basis vector representing the Z-axis of the coordinate system after this matrix's transformation. This is commonly referred to as the "forward" vector. 
For a row-major matrix, this vector is extracted directly from the first three elements of the third row:  (m20, m21, m22) . 
If the matrix includes scaling, this vector's length will reflect that scaling, and it is not guaranteed to be a unit vector. To get a pure direction, normalize this vector. 
The interpretation of this vector as "forward" (e.g., pointing into the screen) depends on the coordinate system's handedness (right-handed vs. left-handed). 
#### Return
A  Vector3  representing the transformed Z-axis, including any scaling.