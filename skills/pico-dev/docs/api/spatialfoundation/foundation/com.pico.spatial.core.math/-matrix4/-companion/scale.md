# scale | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / Companion / scale 
# scale
```kotlin
@JvmStatic
```fun  scale ( scale :  Vector3 ) :  Matrix4 
Creates and returns a 4x4 matrix representing a 3D scaling transformation. 
The scaling factors for the X, Y, and Z axes are provided by the components of the input  scale  vector. 
The resulting matrix will be: 

```
| scale.x  0.0      0.0      0.0 || 0.0      scale.y  0.0      0.0 || 0.0      0.0      scale.z  0.0 || 0.0      0.0      0.0      1.0 |
```
Using zero as a scale factor will collapse the geometry along that axis. Using negative scale factors will result in a reflection (mirroring) along that axis. 
#### Return
A new  Matrix4  instance representing the specified 3D scaling transformation. 
#### Parameters
scale 
A  Vector3  whose  x ,  y , and  z  components define the scaling factors along the respective axes.