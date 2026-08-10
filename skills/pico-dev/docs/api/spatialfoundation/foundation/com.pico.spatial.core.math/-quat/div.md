# div | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / div 
# div
```kotlin
operator fun div(scalar: Float): Quat
```
Overloads the  /  operator to perform element-wise division of this quaternion by a scalar value. 
Each component ( x ,  y ,  z , and  w ) of this quaternion is divided by the  scalar . This is equivalent to multiplying by  1.0f / scalar . 
This function requires the  scalar  to be significantly different from zero (i.e.,  abs(scalar) > 1e-6f ) to prevent division by zero or numerically unstable results. 
Note: If this quaternion represents a rotation (i.e., it is a unit quaternion), dividing by a scalar other than  1.0  or  -1.0  will result in a quaternion that no longer has unit length. 
#### Return
A new  Quat  representing the result of the scalar division. 
#### Parameters
scalar 
The scalar  Float  value to divide this quaternion by. Its absolute value must be greater than  1e-6f . 
#### Throws
Illegal Argument Exception 
if  abs(scalar)  is not greater than  1e-6f .