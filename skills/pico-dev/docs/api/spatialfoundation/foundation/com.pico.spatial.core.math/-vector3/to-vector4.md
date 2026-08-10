# toVector4 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / toVector4 
# toVector4
```kotlin
fun toVector4(): Vector4
```
Converts this 3D vector into a 4D vector, treating it as a point in homogeneous coordinates. 
The w-component of the resulting Vector4 is set to 1.0f. This is the standard representation for a point in 3D space when using 4x4 matrices for affine transformations (like translation, rotation, and scale). A w-component of 1.0f ensures that translations are correctly applied. 
#### Return
A  Vector4  with the same x, y, z components as this vector and a w-component of 1.0f.