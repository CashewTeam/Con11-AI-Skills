# distance | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / Companion / distance 
# distance
```kotlin
@JvmStatic
```fun  distance ( a :  Vector3 ,  b :  Vector3 ) :  Float 
Calculates the Euclidean distance between two 3D vectors. 
The Euclidean distance is the straight-line distance between two points in Euclidean space. It is calculated as the square root of the sum of the squared differences between the corresponding coordinates of the two vectors. 
Formula: sqrt((a.x - b.x)^2 + (a.y - b.y)^2 + (a.z - b.z)^2). 
#### Return
The Euclidean distance between vector 'a' and vector 'b' as a Float. 
#### Parameters
a 
The first 3D vector. 
b 
The second 3D vector.