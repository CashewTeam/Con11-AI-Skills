# slerp | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / Companion / slerp 
# slerp
```kotlin
@JvmStatic
```fun  slerp ( start :  Quat ,  end :  Quat ,  t :  Float ) :  Quat 
Performs Spherical Linear Interpolation (Slerp) between two quaternions,  start  and  end , by an interpolant  t . Slerp provides smooth interpolation of rotations with constant angular velocity along the shortest path on the 4D unit sphere. 
The process involves: 
- 
Clamping the interpolant  t  to the range  [0.0, 1.0] . Exact  t=0.0  or  t=1.0      returns the normalized start or end quaternion respectively. 
- 
Ensuring the interpolation takes the shortest path on the 4D sphere by negating  end      if its dot product with  start  is negative. 
- 
If the two quaternions (after shortest path adjustment) are nearly collinear (i.e.,     the angle between them is very small,  cos(theta)  is close to 1, checked using      1e-6f ), this function falls back to Normalized Linear Interpolation (Nlerp) for     numerical stability and efficiency. 
- 
Otherwise, the standard Slerp formula is used. 
- 
The final result is normalized to ensure it remains a unit quaternion, robust against     potential floating-point inaccuracies. 
Both input quaternions  start  and  end  should ideally be unit quaternions representing rotations for Slerp to be geometrically meaningful. The function attempts to return a normalized quaternion regardless by normalizing at endpoints and for the final result. 
#### Return
A new unit  Quat  representing the spherically interpolated rotation. 
#### Parameters
start 
The starting  Quat  (ideally a unit quaternion). 
end 
The ending  Quat  (ideally a unit quaternion). 
t 
The interpolation factor. Values outside  [0.0, 1.0]  will be clamped.