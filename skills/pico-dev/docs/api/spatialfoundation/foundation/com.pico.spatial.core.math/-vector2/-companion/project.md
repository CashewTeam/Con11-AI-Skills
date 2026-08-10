# project | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / Companion / project 
# project
```kotlin
@JvmStatic
```fun  project ( a :  Vector2 ,  b :  Vector2 ) :  Vector2 
Calculates the vector projection of vector  a  onto vector  b . 
This function projects vector  a  onto the line defined by vector  b . It includes a check to ensure that the target vector  b  is not a zero vector and its squared magnitude  dot(b,b)  is greater than a small positive constant  1e-6f . This check helps prevent numerical instability issues that can arise from projecting onto a very short or zero vector. 
The formula used is equivalent to:  b * (dot(a, b) / dot(b, b)) . 
#### Return
A new  Vector2  instance representing the projection of vector  a  onto vector  b . 
#### Parameters
a 
The vector to be projected. 
b 
The vector onto which  a  is to be projected. Its squared magnitude  dot(b,b)  must be greater than  1e-6f . 
#### Throws
Illegal Argument Exception 
if  dot(b, b)  is less than or equal to  1e-6f .