# angle | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / Companion / angle 
# angle
```kotlin
@JvmStatic
```fun  angle ( from :  Vector2 ,  to :  Vector2 ) :  Float 
Calculates the angle between two 2D vectors and returns it in degrees. This version includes robustness improvements for numerical stability. This function throws an  IllegalArgumentException  if either input vector is a zero vector. The calculated angle represents the shortest angle between the two vectors and is typically in the range  [0, 180]  degrees. 
#### Return
The angle between the two vectors in  degrees , as a  Float . The value will be in the range  [0, 180] . 
#### Parameters
from 
The first vector. Must not be a zero vector. 
to 
The second vector. Must not be a zero vector. 
#### Throws
Illegal Argument Exception 
if either  from  or  to  is a zero vector (i.e., its length is 0).