# faceForward | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / Companion / faceForward 
# faceForward
```kotlin
@JvmStatic
```fun  faceForward ( n :  Vector2 ,  i :  Vector2 ,  nRef :  Vector2 ) :  Vector2 
Orients a normal vector  n  to face towards an incident vector  i , using a reference normal  nRef  to determine the orientation. 
It's typically used in shading calculations to ensure a normal vector consistently points "outward" from a surface, relative to an incident vector (like a view vector or light vector). 
The logic is as follows: 
- 
If the dot product of the reference normal  nRef  and the incident vector  i  is negative ( dot(nRef, i) < 0f ), it means  i  is hitting the "front side" of the surface (the side from which  nRef  is pointing away). In this case, the original normal  n  is returned, assuming it's already oriented correctly for the front side. 
- 
Otherwise ( dot(nRef, i) >= 0f ),  i  is hitting the "back side" of the surface (the side  nRef  is pointing towards), or is tangent to it. In this case, the negated normal  -n  is returned, effectively flipping  n  to orient it correctly for this side. 
The goal is to produce a normal that, when dotted with  i , would typically yield a negative value if  i  is considered a direction  towards  the surface (e.g., a view ray). 
#### Return
Returns  n  if  dot(nRef, i) < 0f , otherwise returns  -n . 
#### Parameters
n 
The normal vector to be potentially oriented. This could be a geometric normal, a shading normal, or any normal that needs consistent orientation. 
i 
The incident vector (e.g., a vector from the camera to the surface, or from a light source to the surface). 
n Ref 
The reference normal, typically the true geometric normal of the surface. It determines which side is considered "front" or "back".