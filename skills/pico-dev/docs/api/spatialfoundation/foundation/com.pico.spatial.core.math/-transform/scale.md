# scale | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Transform / scale 
# scale
```kotlin
fun scale(scale: Vector3): Transform
```
Applies an additional scaling to this transform's current scale and returns a new  Transform  with the combined scale. 
The new scale is calculated by performing an element-wise multiplication of this transform's current scale vector ( this.scale ) with the input  scale  vector. For example,  newScale.x = this.scale.x * scale.x . 
The position and orientation (quaternion) components of the transform remain unchanged. This operation assumes that the  *  operator for  Vector3  performs element-wise multiplication. 
#### Return
A new  Transform  instance with the updated scale, while retaining the original position and orientation. 
#### Parameters
scale 
A  Vector3  representing the additional scaling factors to apply to the current scale components (x, y, z). 
```kotlin
val scale: Vector3
```
The scale vector of the transform.