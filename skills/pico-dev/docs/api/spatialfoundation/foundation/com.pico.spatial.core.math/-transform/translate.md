# translate | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Transform / translate 
# translate
```kotlin
fun translate(translation: Vector3): Transform
```
Applies an additional translation to this transform's current position and returns a new  Transform  with the combined position. 
The new position is calculated by performing an element-wise addition of this transform's current position vector ( this.position ) with the input  translation  vector. 
The orientation (quaternion) and scale components of the transform remain unchanged. This operation assumes that the  +  operator for  Vector3  performs element-wise addition. 
#### Return
A new  Transform  instance with the updated position, while retaining the original orientation and scale. 
#### Parameters
translation 
A  Vector3  representing the translation to apply to the current position.