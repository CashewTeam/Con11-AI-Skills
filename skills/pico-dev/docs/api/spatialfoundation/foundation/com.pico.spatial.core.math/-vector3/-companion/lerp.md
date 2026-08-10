# lerp | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / Companion / lerp 
# lerp
```kotlin
@JvmStatic
```fun  lerp ( a :  Vector3 ,  b :  Vector3 ,  t :  Float ) :  Vector3 
Performs a linear interpolation between two vectors  a  and  b  by an interpolant  t . 
The interpolant  t  is clamped to the range  [0.0, 1.0] . When  t = 0.0 , this function returns  a . When  t = 1.0 , this function returns  b . When  0.0 < t < 1.0 , the return value is a point on the line segment between  a  and  b . This function does not extrapolate (i.e.,  t  values outside  [0.0, 1.0]  are clamped to this range). 
The calculation is  a + (b - a) * t_clamped . 
#### Return
The interpolated  Vector3 . 
#### Parameters
a 
The starting vector. 
b 
The ending vector. 
t 
The interpolation factor, which will be clamped to the  [0.0, 1.0]  range.