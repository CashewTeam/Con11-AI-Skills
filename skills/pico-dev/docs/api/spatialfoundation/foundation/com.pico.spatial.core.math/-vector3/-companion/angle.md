# angle | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / Companion / angle 
# angle
```kotlin
@JvmStatic
```fun  angle ( from :  Vector3 ,  to :  Vector3 ) :  Float 
Calculates the angle in degrees between two 3D vectors. 
The angle is computed using the dot product of the vectors and their magnitudes. This function includes checks to ensure that neither input vector is a zero vector and clamps the cosine value before applying  acos  to enhance numerical stability. The result is the shortest angle between the two vectors, typically in the range  [0, 180]  degrees. 
#### Return
The angle between the two vectors in  degrees , as a  Float . The value will be in the range  [0, 180] . 
#### Parameters
from 
The first vector. Must not be a zero-length vector. 
to 
The second vector. Must not be a zero-length vector. 
#### Throws
Illegal Argument Exception 
if either  from  or  to  has a zero length.