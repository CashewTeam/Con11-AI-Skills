# slerpLongPath | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / Companion / slerpLongPath 
# slerpLongPath
```kotlin
@JvmStatic
```fun  slerpLongPath ( start :  Quat ,  end :  Quat ,  t :  Float ) :  Quat 
Performs Spherical Linear Interpolation (Slerp) between two quaternions,  start  and  end , by an interpolant  t , ensuring that the interpolation takes the  long path  if a shorter rotational path exists. 
The "long path" means that if the direct 3D rotation angle between  start  and  end  is less than 180 degrees, this function will interpolate through an angle greater than 180 degrees (effectively going "the other way around" on the 4D sphere that represents rotations). 
The process involves: 
- 
Clamping  t  to  [0.0, 1.0] . Exact  t=0  or  t=1  returns normalized inputs. 
- 
Adjusting  end  (by negating it if  dot(start, end) > 0 ) to ensure the 4D angle used     for Slerp is obtuse (>= 90 degrees), which corresponds to the long path for 3D     rotation. 
- 
If the  start  and the (adjusted)  end  quaternions are nearly opposite (4D angle     close to 180 degrees,  cosThetaEffective  close to -1), this function falls back to     Normalized Linear Interpolation (Nlerp) for numerical stability. 
- 
Otherwise, the standard Slerp formula is applied using the obtuse 4D angle. 
- 
The final result is normalized to ensure it remains a unit quaternion. 
Both  start  and  end  should ideally be unit quaternions. 
#### Return
A new unit  Quat  representing the spherically interpolated rotation along the long path. 
#### Parameters
start 
The starting  Quat  (typically a unit quaternion). 
end 
The ending  Quat  (typically a unit quaternion). 
t 
The interpolation factor. Will be clamped to  [0.0, 1.0] .