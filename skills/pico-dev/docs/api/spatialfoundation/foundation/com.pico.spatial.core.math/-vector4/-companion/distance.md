# distance | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 / Companion / distance 
# distance
```kotlin
@JvmStatic
```fun  distance ( a :  Vector4 ,  b :  Vector4 ) :  Float 
Calculates the Euclidean distance between two 4D vectors,  a  and  b . 
The distance is computed as the square root of the sum of the squared differences between their corresponding components:  sqrt((a.x-b.x)^2 + (a.y-b.y)^2 + (a.z-b.z)^2 + (a.w-b.w)^2) . 
#### Return
The Euclidean distance between the two vectors as a  Float . 
#### Parameters
a 
The first  Vector4 . 
b 
The second  Vector4 .