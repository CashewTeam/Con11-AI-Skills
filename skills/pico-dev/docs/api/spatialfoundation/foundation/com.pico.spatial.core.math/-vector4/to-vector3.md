# toVector3 | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 / toVector3 
# toVector3
```kotlin
fun toVector3(): Vector3
```
Converts this 4D vector to a 3D vector by discarding the w-component. 
This is a straightforward truncation, useful when you want to get the 3D spatial coordinates from a 4D vector representation (like one resulting from a matrix transformation before perspective division) and are not concerned with the w-component. Note that this is a lossy conversion as the  w  component is ignored. 
#### Return
A  Vector3  containing the x, y, and z components of this vector.