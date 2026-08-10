# slerpUnclamped | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Vector3 / Companion / slerpUnclamped 
# slerpUnclamped
```kotlin
@JvmStatic
```fun  slerpUnclamped ( a :  Vector3 ,  b :  Vector3 ,  t :  Float ) :  Vector3 
Performs unclamped spherical linear interpolation (slerp) between two 3D vectors. 
This method interpolates along the shortest great-circle arc between two vectors. The interpolation parameter  t  is not clamped to 0, 1, allowing extrapolation. 
Special cases handling: 
- 
When vectors are nearly parallel: falls back to linear interpolation. 
- 
When vectors are nearly opposite: uses a perpendicular rotation plane. 
#### Return
Interpolated vector. 
#### Parameters
a 
Start vector (unit vector expected for accurate results). 
b 
End vector (unit vector expected for accurate results). 
t 
Interpolation/extrapolation parameter (0 = full a, 1 = full b).