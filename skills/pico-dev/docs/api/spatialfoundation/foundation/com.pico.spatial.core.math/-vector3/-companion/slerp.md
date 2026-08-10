# slerp | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / Companion / slerp 
# slerp
```kotlin
@JvmStatic
```fun  slerp ( a :  Vector3 ,  b :  Vector3 ,  t :  Float ) :  Vector3 
Performs Spherical Linear Interpolation between two 3D vectors  a  and  b  by an interpolant  t . 
Precondition : For a geometrically correct spherical interpolation that preserves magnitude (if inputs are normalized) and interpolates along the shortest arc on a sphere, input vectors  a  and  b  should ideally be  normalized  (unit length). If they are not, the interpolation will occur, but the path may not be a true arc on a sphere of constant radius, and magnitudes will also be interpolated in a complex way. 
The interpolant  t  is required to be in the range  [0.0, 1.0] . This implementation handles cases where  a  and  b  are nearly collinear by falling back to linear interpolation ( lerp ) to maintain numerical stability. 
#### Return
The spherically interpolated  Vector3 . 
#### Parameters
a 
The starting vector. Should ideally be normalized. 
b 
The ending vector. Should ideally be normalized. 
t 
The interpolation factor, in the range  [0.0, 1.0] . 
#### Throws
Illegal Argument Exception 
if  t  is not in the range  [0.0, 1.0] .