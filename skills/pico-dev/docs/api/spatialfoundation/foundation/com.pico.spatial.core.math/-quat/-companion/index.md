# Companion | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  Quat . 
Members 
## Functions
dot 
```kotlin
@JvmStatic
```fun  dot ( a :  Quat ,  b :  Quat ) :  Float 
Calculates the dot product (scalar product) of two quaternions,  a  and  b . 
identity 
```kotlin
@JvmStatic
```fun  identity ( ) :  Quat 
Gets the  Quat  instance that represents the identity. 
nlerp 
```kotlin
@JvmStatic
```fun  nlerp ( start :  Quat ,  end :  Quat ,  t :  Float ) :  Quat 
Performs Normalized Linear Interpolation (Nlerp) between two quaternions,  start  and  end , using the interpolation factor  t . This method is suitable for efficiently interpolating 3D rotations. 
slerp 
```kotlin
@JvmStatic
```fun  slerp ( start :  Quat ,  end :  Quat ,  t :  Float ) :  Quat 
Performs Spherical Linear Interpolation (Slerp) between two quaternions,  start  and  end , by an interpolant  t . Slerp provides smooth interpolation of rotations with constant angular velocity along the shortest path on the 4D unit sphere. 
slerp Long Path 
```kotlin
@JvmStatic
```fun  slerpLongPath ( start :  Quat ,  end :  Quat ,  t :  Float ) :  Quat 
Performs Spherical Linear Interpolation (Slerp) between two quaternions,  start  and  end , by an interpolant  t , ensuring that the interpolation takes the  long path  if a shorter rotational path exists.