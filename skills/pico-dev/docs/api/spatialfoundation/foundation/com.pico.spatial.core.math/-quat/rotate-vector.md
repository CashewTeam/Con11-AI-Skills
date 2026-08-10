# rotateVector | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / rotateVector 
# rotateVector
```kotlin
fun rotateVector(vector: Vector3): Vector3
```
Rotates the given Vector3 by this quaternion. 
This quaternion ( this ) should be a unit quaternion to represent a pure rotation. If this quaternion is not normalized, the transformation will also include scaling. The rotation is applied using the formula derived from  v' = q * v * conjugate(q) , often implemented efficiently as  v_rotated = v + 2w * (u × v) + 2 * (u × (u × v)) , where  q = (u, w)  (u is the vector part, w is the scalar part) and  v  is the vector. 
#### Return
A new  Vector3  instance representing the rotated vector. 
#### Parameters
vector 
The  Vector3  to be rotated.