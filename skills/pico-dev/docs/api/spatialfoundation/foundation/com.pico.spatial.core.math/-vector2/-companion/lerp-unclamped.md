# lerpUnclamped | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / Companion / lerpUnclamped 
# lerpUnclamped
```kotlin
@JvmStatic
```fun  lerpUnclamped ( a :  Vector2 ,  b :  Vector2 ,  t :  Float ) :  Vector2 
Performs unclamped linear interpolation between two 2D vectors,  a  and  b . 
This function calculates a point along the infinite line defined by vectors  a  (as the point when  t=0 ) and  b  (as the point when  t=1 ). Unlike a standard clamped  lerp , the interpolation factor  t  is not restricted to the  [0.0, 1.0]  range. This means the function can extrapolate beyond the segment connecting  a  and  b . 
The formula used is:  result = a + (b - a) * t . 
#### Return
A new  Vector2  instance representing the linearly interpolated or extrapolated vector. 
#### Parameters
a 
The starting vector (value when  t=0 ). 
b 
The ending vector (value when  t=1 ). 
t 
The interpolation factor. This value is used as is, without clamping.