# faceForward | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / Companion / faceForward 
# faceForward
```kotlin
@JvmStatic
```fun  faceForward ( n :  Vector3 ,  i :  Vector3 ,  nRef :  Vector3 ) :  Vector3 
Orients a vector  n  to face in the direction opposite to an incident vector  i , using  nRef  as a reference to determine if  i  is arriving from the front or back side. 
If  dot(nRef, i)  is negative, it means  i  is considered to be on the "front side" (the side  nRef  points away from, assuming  i  points towards the surface), and  n  is returned as is. Otherwise,  i  is considered to be on the "back side" (or grazing the surface), and  -n  (the negation of  n ) is returned. 
This is typically used to ensure a normal vector used in lighting calculations correctly faces the incident light or view vector. 
#### Return
Returns  n  if  dot(nRef, i) < 0.0 , otherwise returns  -n . 
#### Parameters
n 
The vector to orient, typically a normal vector. 
i 
The incident vector (e.g., view vector or light vector pointing towards the surface). 
n Ref 
The reference normal, typically the geometric normal of the surface, used to determine the orientation of  i  relative to the surface.