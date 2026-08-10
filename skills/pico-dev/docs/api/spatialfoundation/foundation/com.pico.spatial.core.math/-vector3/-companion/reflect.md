# reflect | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / Companion / reflect 
# reflect
```kotlin
@JvmStatic
```fun  reflect ( i :  Vector3 ,  n :  Vector3 ) :  Vector3 
Calculates the reflection vector of an incident vector 'i' across a surface defined by its normal 'n'. 
The reflection is calculated using the formula: R = I - 2 * dot(I, N) * N, where 'I' is the incident vector and 'N' is the surface normal. 
For a correct reflection, the normal vector 'n' should ideally be a unit vector (normalized). If 'n' is not normalized, the direction of the reflection will be correct, but its magnitude might not be what is intuitively expected (i.e., it won't preserve the magnitude of 'i' relative to the surface interaction). 
#### Return
The reflected vector as a new Vector3 instance. 
#### Parameters
i 
The incident vector (the vector to be reflected). 
n 
The normal vector of the surface off which the incident vector reflects. This vector should typically be normalized for physically accurate reflection magnitude.