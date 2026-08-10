# length | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / length 
# length
```kotlin
fun length(): Float
```
Calculates the length (magnitude or norm) of this quaternion. 
The length is calculated as the square root of the sum of the squares of its four components (x, y, z, and w). For a quaternion to represent a pure rotation, it should be a "unit quaternion," meaning its length should be 1.0. 
#### Return
The length of the quaternion as a Float.