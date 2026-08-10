# normalize | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / normalize 
# normalize
```kotlin
fun normalize(): Vector3
```
Normalizes the  Vector3  instance. 
This method returns a unit vector in the same direction as this  Vector3  instance. If the vector's length is zero, it returns a copy of the original vector. 
#### Return
The normalized  Vector3  instance if the length is greater than zero; otherwise, a copy of the original  Vector3  instance is returned.