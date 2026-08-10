# normalize | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / normalize 
# normalize
```kotlin
fun normalize(): Vector2
```
Normalizes the  Vector2  instance. 
This method returns a unit vector in the same direction as this  Vector2  instance. If the vector's length is zero, it returns a copy of the original vector. 
#### Return
The normalized  Vector2  instance if the length is greater than zero; otherwise, a copy of the original Vector2 instance is returned.