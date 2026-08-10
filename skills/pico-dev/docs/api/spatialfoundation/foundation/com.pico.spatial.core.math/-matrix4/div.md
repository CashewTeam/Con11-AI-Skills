# div | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / div 
# div
```kotlin
operator fun div(scale: Float): Matrix4
```
Overloads the  /  operator to perform element-wise division of this matrix by a scalar value. 
Each component of the resulting matrix is the result of dividing the corresponding component of this matrix by the  scale  factor. 
This function requires the  scale  factor to be significantly different from zero (i.e.,  abs(scale) > 1e-6f ) to prevent division by zero or numerically unstable results. 
#### Return
A new  Matrix4  representing the result of the scalar division. 
#### Parameters
scale 
The scalar  Float  value to divide this matrix by. Its absolute value must be greater than  1e-6f . 
#### Throws
Illegal Argument Exception 
if  abs(scale)  is not greater than  1e-6f .