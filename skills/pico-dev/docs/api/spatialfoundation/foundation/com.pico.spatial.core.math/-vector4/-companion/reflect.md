# reflect | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 / Companion / reflect 
# reflect
```kotlin
@JvmStatic
```fun  reflect ( i :  Vector4 ,  n :  Vector4 ) :  Vector4 
Calculates the reflection of an incident vector  i  across a surface defined by the normal vector  n . 
The reflection is computed using the formula:  R = I - 2 * N * dot(I, N) . 
This function  requires  the normal vector  n  to be a  unit vector (normalized)  for the reflection to be geometrically accurate (where the angle of incidence equals the angle of reflection). A check is performed using  1e-6f  tolerance to ensure  n  is normalized; an  IllegalArgumentException  is thrown if this precondition is not met. 
#### Return
The reflected  Vector4 . 
#### Parameters
i 
The incident  Vector4 . 
n 
The normal  Vector4  of the reflection surface.  Must be a unit vector  (its length must be approximately  1.0f  within  1e-6f  tolerance). 
#### Throws
Illegal Argument Exception 
if the normal vector  n  is not normalized (i.e.,  abs(n.length() - 1.0f) >= 1e-6f ).