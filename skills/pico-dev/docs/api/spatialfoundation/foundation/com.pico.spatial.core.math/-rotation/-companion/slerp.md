# slerp | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Rotation / Companion / slerp 
# slerp
```kotlin
@JvmStatic
```fun  slerp ( from :  Rotation ,  to :  Rotation ,  t :  Float ,  path :  Rotation.Companion.SlerpPath  =  SlerpPath.SHORTEST ) :  Rotation 
Performs Spherical Linear Interpolation (Slerp) between two rotations. 
Slerp provides smooth interpolation with constant angular velocity. Input quaternions are internally normalized at endpoints or if used in Nlerp fallback. The final result is also normalized for robustness. 
#### Return
The spherically interpolated  Rotation . 
#### Parameters
from 
The starting  Rotation . 
to 
The ending  Rotation . 
t 
The interpolation factor, clamped to the range  [0.0, 1.0] . 
path 
Specifies whether to interpolate along the  SHORTEST  or  LONGEST  arc. Defaults to  SHORTEST .