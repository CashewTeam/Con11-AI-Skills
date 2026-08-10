# rotateXByDegrees | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / Companion / rotateXByDegrees 
# rotateXByDegrees
```kotlin
@JvmStatic
```fun  rotateXByDegrees ( degrees :  Float ) :  Matrix4 
Creates and returns a 4x4 matrix representing a rotation around the X-axis. The input angle is specified in  degrees . 
The input  degrees  must be a finite floating-point number. 
This transformation rotates points counter-clockwise around the X-axis when viewed from the positive X-axis towards the origin (assuming a right-handed coordinate system). The function internally converts the angle from degrees to radians using  EulerAngles.degreeToRadian()  before applying trigonometric functions. 
The resulting matrix structure is: 

```
| 1.0  0.0     0.0      0.0 || 0.0  cos(rad) -sin(rad)   0.0 || 0.0  sin(rad)  cos(rad)   0.0 || 0.0  0.0     0.0      1.0 |
```
where  rad  is the input angle converted to radians. 
#### Return
A new  Matrix4  instance representing the specified rotation around the X-axis. 
#### Parameters
degrees 
The rotation angle in  degrees . Must be a finite number. 
#### Throws
Illegal Argument Exception 
if  degrees  is not a finite number (NaN or Infinity).