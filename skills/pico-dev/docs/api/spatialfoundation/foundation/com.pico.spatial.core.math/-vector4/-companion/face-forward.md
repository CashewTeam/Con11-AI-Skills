# faceForward | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 / Companion / faceForward 
# faceForward
```kotlin
@JvmStatic
```fun  faceForward ( n :  Vector4 ,  i :  Vector4 ,  nRef :  Vector4 ) :  Vector4 
Orients a 4D vector  n  to face in a direction consistent with an incident vector  i , using a reference vector  nRef  to determine orientation. 
If the 4D dot product of  nRef  and  i  is negative,  n  is returned. Otherwise,  -n  (the negation of  n ) is returned. 
This is typically used to ensure a normal-like vector correctly orients itself with respect to an incident direction, based on a surface's reference orientation. The geometric interpretation in 4D depends on the specific meaning of the components. 
#### Return
Returns  n  if  dot(nRef, i) < 0.0f , otherwise returns  -n . 
#### Parameters
n 
The 4D vector to orient, often a normal-like vector. 
i 
The incident 4D vector. 
n Ref 
The reference 4D vector, typically a geometric normal-like orientation.