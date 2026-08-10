# lerp | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector2 / Companion / lerp 
# lerp
```kotlin
@JvmStatic
```fun  lerp ( a :  Vector2 ,  b :  Vector2 ,  t :  Float ) :  Vector2 
Performs linear interpolation between two 2D vectors,  a  and  b . 
Linear interpolation finds a point along the straight line segment connecting vector  a  (the start point) and vector  b  (the end point). The parameter  t  determines where on this segment the interpolated point lies. 
The formula used is:  result = a + (b - a) * t_clamped , where  t_clamped  is the interpolation factor  t  clamped to the range  [0.0, 1.0] . 
#### Return
A new  Vector2  instance representing the linearly interpolated vector. 
#### Parameters
a 
The starting vector (interpolated from, when  t=0 ). 
b 
The ending vector (interpolated towards, when  t=1 ). 
t 
The interpolation factor. This value will be clamped to the range  [0.0, 1.0]  before being used in the calculation.