# cross | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / Companion / cross 
# cross
```kotlin
@JvmStatic
```fun  cross ( a :  Vector2 ,  b :  Vector2 ) :  Float 
Calculates the 2D cross product (also known as the perpendicular dot product or z-component of the 3D cross product) of two 2D vectors. 
The 2D cross product is a scalar value calculated as:  a.x * b.y - a.y * b.x . 
Geometric Interpretation: 
- 
The magnitude of this scalar ( abs(a.x * b.y - a.y * b.x) ) is equal to the area of the parallelogram formed by the two vectors  a  and  b . 
- 
The sign of the result indicates the orientation of vector  b  relative to vector  a  (assuming a standard Cartesian coordinate system where the positive Y-axis is 90 degrees counter-clockwise from the positive X-axis): 
- 
If  cross(a, b) > 0 : vector  b  is counter-clockwise from vector  a . 
- 
If  cross(a, b) < 0 : vector  b  is clockwise from vector  a . 
- 
If  cross(a, b) == 0 : vectors  a  and  b  are collinear (i.e., they are parallel or antiparallel, lying on the same line). This means the area of the parallelogram is zero. 
This value is also equivalent to the z-component of the 3D cross product if  a  and  b  were considered as 3D vectors in the xy-plane (i.e.,  A = (a.x, a.y, 0)  and  B = (b.x, b.y, 0) ). The 3D cross product  A x B  would be  (0, 0, a.x*b.y - a.y*b.x) . 
It is related to the sine of the angle  θ  between the vectors:  cross(a,b) = |a| |b| sin(θ) , where  θ  is the signed angle from  a  to  b . 
#### Return
The scalar 2D cross product as a Float. 
#### Parameters
a 
The first 2D vector. 
b 
The second 2D vector.