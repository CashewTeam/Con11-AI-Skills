# normalize | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 / normalize 
# normalize
```kotlin
fun normalize(): Vector4
```
Normalizes the  Vector4  instance. 
This method returns a unit vector in the same direction as this  Vector4  instance. If the vector's length is zero, it returns a copy of the original vector. 
#### Return
The normalized  Vector4  instance if the length is greater than zero; otherwise, a copy of the original  Vector4  instance is returned.