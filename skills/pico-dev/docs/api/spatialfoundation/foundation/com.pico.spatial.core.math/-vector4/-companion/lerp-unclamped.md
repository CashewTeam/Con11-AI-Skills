# lerpUnclamped | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 / Companion / lerpUnclamped 
# lerpUnclamped
```kotlin
@JvmStatic
```fun  lerpUnclamped ( a :  Vector4 ,  b :  Vector4 ,  t :  Float ) :  Vector4 
Performs an unclamped linear interpolation between two 4D vectors  a  and  b  by an interpolation factor  t . 
- 
When  t = 0.0 , this function returns  a . 
- 
When  t = 1.0 , this function returns  b . 
- 
When  0.0 < t < 1.0 , the return value is a point on the line segment strictly between  a  and  b . 
- 
When  t < 0.0  or  t > 1.0 , the return value is a point on the infinite line defined by  a  and  b , extrapolated beyond the segment  [a, b] . 
The calculation is  a + (b - a) * t . 
#### Return
The interpolated or extrapolated  Vector4 . 
#### Parameters
a 
The starting  Vector4  (value when  t=0 ). 
b 
The "ending"  Vector4  (value when  t=1 ). 
t 
The interpolation/extrapolation factor. It is not clamped.