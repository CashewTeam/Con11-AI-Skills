# rotateZByDegrees | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / Companion / rotateZByDegrees 
# rotateZByDegrees
```kotlin
@JvmStatic
```fun  rotateZByDegrees ( degrees :  Float ) :  Matrix4 
Creates and returns a 4x4 matrix representing a rotation around the Z-axis. The input angle is specified in  degrees . 
This transformation rotates points counter-clockwise around the Z-axis when viewed from the positive Z-axis towards the origin (standard right-handed coordinate system convention). The function internally converts the angle from degrees to radians using  EulerAngles.degreeToRadian()  before applying trigonometric functions. 
The input  degrees  must be a finite floating-point number. 
The resulting matrix structure is: 

```
| cos(rad)  -sin(rad)  0.0  0.0 || sin(rad)   cos(rad)  0.0  0.0 || 0.0        0.0       1.0  0.0 || 0.0        0.0       0.0  1.0 |
```
where  rad  is the input angle converted to radians. 
#### Return
A new  Matrix4  instance representing the specified counter-clockwise rotation around the Z-axis. 
#### Parameters
degrees 
The rotation angle in  degrees . Must be a finite number. 
#### Throws
Illegal Argument Exception 
if  degrees  is not a finite number (NaN or Infinity).