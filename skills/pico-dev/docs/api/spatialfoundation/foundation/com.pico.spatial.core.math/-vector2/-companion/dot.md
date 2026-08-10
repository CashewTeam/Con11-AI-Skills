# dot | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / Companion / dot 
# dot
```kotlin
@JvmStatic
```fun  dot ( a :  Vector2 ,  b :  Vector2 ) :  Float 
Calculates the dot product (scalar product) of two 2D vectors. 
The dot product is a scalar value that can be used to determine the angular relationship between two vectors. It is calculated as the sum of the products of their corresponding components:  a.x * b.x + a.y * b.y . 
Geometrically, the dot product is related to the cosine of the angle between the two vectors:  A · B = |A| |B| cos(θ) , where  θ  is the angle between vectors A and B, and  |A|  and  |B|  are their magnitudes. 
Key properties and uses: 
- 
If the dot product is 0, the vectors are orthogonal (perpendicular), assuming neither vector is zero. 
- 
If the dot product is positive, the angle between the vectors is acute (< 90 degrees). 
- 
If the dot product is negative, the angle between the vectors is obtuse (> 90 degrees). 
- 
The dot product of a vector with itself ( dot(v, v) ) yields the square of its magnitude ( |v|^2 ). 
- 
It can be used to project one vector onto another. 
#### Return
The dot product of vectors 'a' and 'b' as a Float. 
#### Parameters
a 
The first 2D vector. 
b 
The second 2D vector.