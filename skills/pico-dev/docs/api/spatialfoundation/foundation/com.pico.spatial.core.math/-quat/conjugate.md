# conjugate | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / conjugate 
# conjugate
```kotlin
fun conjugate(): Quat
```
Calculates and returns the conjugate of this quaternion. 
The conjugate of a quaternion  q = w + xi + yj + zk  is  q* = w - xi - yj - zk . It has the same scalar part ( w ) and negated vector part ( -x, -y, -z ). 
For a unit quaternion (which is typically used to represent rotations), its conjugate is also its inverse ( q* = q⁻¹ ). 
#### Return
A new  Quat  instance representing the conjugate of this quaternion.