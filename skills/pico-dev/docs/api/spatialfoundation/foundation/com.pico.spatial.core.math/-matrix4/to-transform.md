# toTransform | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / toTransform 
# toTransform
```kotlin
fun toTransform(): Transform
```
Converts the  Matrix4  instance to a  Transform  object. 
The resulting  Transform  object encapsulates the position, rotation, and scale information extracted from this matrix. Specifically: 
- 
The  position  property of the  Transform  is obtained from the  position  property of this matrix, which represents the translation component of the matrix. 
- 
The  rotation  property of the  Transform  is obtained from the  rotation  property of this matrix, which is converted to a  Quat  representing the rotation. 
- 
The  scale  property of the  Transform  is obtained from the  scale  property of this matrix, which represents the scaling factors along the local X, Y, and Z axes. 
#### Return
A new  Transform  object containing the position, rotation, and scale information extracted from this matrix.