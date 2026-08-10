# rotateByDegrees | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix3 / Companion / rotateByDegrees 
# rotateByDegrees
```kotlin
@JvmStatic
```fun  rotateByDegrees ( angleInDegrees :  Float ) :  Matrix3 
Creates and returns a 3x3 matrix representing a 2D rotation in the XY-plane (equivalent to a rotation around the Z-axis in a 3D context). 
A positive angle results in a counter-clockwise rotation when looking down the Z-axis towards the origin (standard right-handed system convention for Z-axis rotation). The Z-coordinates of transformed vectors are unaffected by this matrix. 
The input angle is specified in  degrees  and is converted to radians internally for trigonometric calculations. 
The resulting matrix is: 

```
| cos(rad)  -sin(rad)  0.0 || sin(rad)   cos(rad)  0.0 || 0.0        0.0       1.0 |
```
where  rad  is the input angle converted to radians. 
#### Return
A new  Matrix3  instance representing the specified rotation. 
#### Parameters
angle In Degrees 
The rotation angle in degrees.