# project | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / Companion / project 
# project
```kotlin
@JvmStatic
```fun  project ( a :  Vector3 ,  b :  Vector3 ) :  Vector3 
Calculates the vector projection of vector  a  onto vector  b . 
This function projects vector  a  onto the line defined by vector  b . It includes a check using a small positive constant  1e-6f  to ensure that the target vector  b  is not a zero vector and its squared magnitude  dot(b,b)  is sufficiently large. This helps prevent numerical instability issues that can arise from projecting onto a very short or zero vector. 
The formula applied is equivalent to:  b * (dot(a, b) / dot(b, b)) . 
#### Return
A new  Vector3  instance representing the projection of vector  a  onto vector  b . 
#### Parameters
a 
The vector to be projected. 
b 
The vector onto which  a  is to be projected. Its squared magnitude  dot(b,b)  must be greater than  EPSILON . 
#### Throws
Illegal Argument Exception 
if  dot(b, b)  is less than or equal to  1e-6f .