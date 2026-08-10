# lerp | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector4 / Companion / lerp 
# lerp
```kotlin
@JvmStatic
```fun  lerp ( a :  Vector4 ,  b :  Vector4 ,  t :  Float ) :  Vector4 
Performs a linear interpolation between two 4D vectors  a  and  b  by an interpolant  t . 
The interpolant  t  is clamped to the range  [0.0, 1.0] . 
- 
When  t = 0.0  (or less), this function returns  a . 
- 
When  t = 1.0  (or greater), this function returns  b . 
- 
When  0.0 < t < 1.0 , the return value is a point on the line segment strictly between  a  and  b . 
This function does not extrapolate;  t  values outside the  [0.0, 1.0]  range are clamped to this range before interpolation. The calculation is  a + (b - a) * t_clamped . 
#### Return
The interpolated  Vector4 . 
#### Parameters
a 
The starting  Vector4 . 
b 
The ending  Vector4 . 
t 
The interpolation factor. Will be clamped to the  [0.0, 1.0]  range.