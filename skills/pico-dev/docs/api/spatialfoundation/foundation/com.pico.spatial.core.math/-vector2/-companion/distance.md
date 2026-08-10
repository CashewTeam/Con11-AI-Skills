# distance | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / Companion / distance 
# distance
```kotlin
@JvmStatic
```fun  distance ( a :  Vector2 ,  b :  Vector2 ) :  Float 
Calculates the Euclidean distance between two 2D points (represented by vectors). 
The distance is determined by finding the length (magnitude) of the vector that results from subtracting vector  b  from vector  a  (i.e., the vector pointing from  b  to  a ). 
Mathematically, this is equivalent to:  sqrt((a.x - b.x)^2 + (a.y - b.y)^2) . 
#### Return
The Euclidean distance between point  a  and point  b  as a Float. 
#### Parameters
a 
The first 2D point (or vector). 
b 
The second 2D point (or vector).