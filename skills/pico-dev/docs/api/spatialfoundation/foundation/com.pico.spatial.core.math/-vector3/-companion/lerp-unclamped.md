# lerpUnclamped | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / Companion / lerpUnclamped 
# lerpUnclamped
```kotlin
@JvmStatic
```fun  lerpUnclamped ( a :  Vector3 ,  b :  Vector3 ,  t :  Float ) :  Vector3 
Performs an unclamped linear interpolation between two vectors  a  and  b  by an interpolant  t . 
The interpolant  t  is not clamped. This means if  t  is outside the  [0.0, 1.0]  range, the function will perform extrapolation. 
- 
When  t = 0.0 , this function returns  a . 
- 
When  t = 1.0 , this function returns  b . 
- 
When  0.0 < t < 1.0 , the return value is a point on the line segment between  a  and  b . 
- 
When  t < 0.0  or  t > 1.0 , the return value is a point on the infinite line defined by  a  and  b , extrapolated beyond the segment. 
The calculation is  a + (b - a) * t . 
#### Return
The interpolated or extrapolated  Vector3 . 
#### Parameters
a 
The starting vector (value when  t=0 ). 
b 
The "ending" vector (value when  t=1 ). 
t 
The interpolation/extrapolation factor. It is not clamped.