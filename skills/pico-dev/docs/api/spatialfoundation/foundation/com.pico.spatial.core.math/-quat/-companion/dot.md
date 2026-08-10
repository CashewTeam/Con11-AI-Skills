# dot | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / Companion / dot 
# dot
```kotlin
@JvmStatic
```fun  dot ( a :  Quat ,  b :  Quat ) :  Float 
Calculates the dot product (scalar product) of two quaternions,  a  and  b . 
The dot product is computed as the sum of the products of their corresponding components ( a.x*b.x + a.y*b.y + a.z*b.z + a.w*b.w ). 
For two unit quaternions, their dot product is equal to  cos(angle/2) , where  angle  is the angle of rotation that transforms the orientation represented by one quaternion to that of the other. It provides a measure of similarity between the two rotations. 
#### Return
The dot product of the two quaternions as a  Float  scalar value. 
#### Parameters
a 
The first  Quat . 
b 
The second  Quat .