# nlerp | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / Companion / nlerp 
# nlerp
```kotlin
@JvmStatic
```fun  nlerp ( start :  Quat ,  end :  Quat ,  t :  Float ) :  Quat 
Performs Normalized Linear Interpolation (Nlerp) between two quaternions,  start  and  end , using the interpolation factor  t . This method is suitable for efficiently interpolating 3D rotations. 
nlerp is generally faster than Slerp but does not guarantee constant angular velocity. It's a good approximation, especially for small rotational differences. 
#### Return
A new unit  Quat  representing the normalized linear interpolation. 
#### Parameters
start 
The starting  Quat  (typically a unit quaternion representing a rotation). 
end 
The ending  Quat  (typically a unit quaternion representing a rotation). 
t 
The interpolation factor. Will be clamped to the  [0.0, 1.0]  range.