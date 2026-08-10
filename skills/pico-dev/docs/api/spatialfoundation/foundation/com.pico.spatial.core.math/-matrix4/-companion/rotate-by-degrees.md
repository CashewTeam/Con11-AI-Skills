# rotateByDegrees | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / Companion / rotateByDegrees 
# rotateByDegrees
```kotlin
@JvmStatic
```fun  rotateByDegrees ( degrees :  Float ,  axis :  Vector3 ) :  Matrix4 
Creates and returns a 4x4 matrix representing a rotation around a given  axis  by an angle specified in  degrees . 
The rotation follows the right-hand rule: if the thumb of the right hand points along the  axis  direction, a positive angle results in a counter-clockwise rotation. 
The input  degrees  must be a finite floating-point number. The input  axis  must be a non-zero vector (its length is checked against  1e-6f ); it will be normalized internally. This function uses Rodrigues' rotation formula to construct the matrix. 
#### Return
A new  Matrix4  instance representing the specified rotation. 
#### Parameters
degrees 
The rotation angle in  degrees . Must be a finite number. 
axis 
The 3D vector representing the axis of rotation. Must be non-zero. 
#### Throws
Illegal Argument Exception 
if  degrees  is not a finite number, or if the  axis  vector is a zero vector or its length is not greater than  1e-6f .