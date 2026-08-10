# rotate | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Transform / rotate 
# rotate
```kotlin
fun rotate(rotation: Quat): Transform
```
Applies an additional rotation to this transform's current orientation and returns a new  Transform  with the combined rotation. 
The new orientation is calculated by multiplying this transform's current orientation quaternion ( this.quaternion ) with the input  rotation  quaternion ( this.quaternion * rotation ). The position and scale components of the transform remain unchanged. 
If you want to use the result to represent a pure rotation, it is assumed that both  this.quaternion  and the input  rotation  are unit quaternions. The product of two unit quaternions is also a unit quaternion. 
#### Return
A new  Transform  instance with the updated orientation, while retaining the original position and scale. 
#### Parameters
rotation 
A  Quat  representing the additional rotation to apply. It should be a unit quaternion if a pure rotation is intended.