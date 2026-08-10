# reflect | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / Companion / reflect 
# reflect
```kotlin
@JvmStatic
```fun  reflect ( i :  Vector2 ,  n :  Vector2 ) :  Vector2 
Calculates the reflection of an incident vector 'i' across a surface defined by its normal 'n'. 
The reflection vector  R  is calculated using the formula:  R = I - 2 * dot(I, N) * N , where  I  is the incident vector and  N  is the surface normal. 
For this formula to produce a physically accurate reflection (where the angle of incidence equals the angle of reflection), the normal vector 'n'  must be a unit vector  (i.e., its length must be 1). If 'n' is not normalized, the direction of the reflection will still be generally correct relative to the line defined by 'n', but the result might not correspond to a standard elastic collision reflection. 
#### Return
The reflected vector as a new  Vector2  instance. 
#### Parameters
i 
The incident vector (the vector to be reflected). 
n 
The normal vector of the surface.  Should be a unit vector for accurate reflection .