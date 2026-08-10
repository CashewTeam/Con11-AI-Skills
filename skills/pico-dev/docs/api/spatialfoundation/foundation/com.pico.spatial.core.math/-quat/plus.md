# plus | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / plus 
# plus
```kotlin
operator fun plus(other: Quat): Quat
```
Overloads the  +  operator to perform component-wise addition of this quaternion with another quaternion. 
Each component ( x ,  y ,  z , and  w ) of the resulting quaternion is the sum of the corresponding components of this quaternion and the  other  quaternion. 
Note: If both input quaternions are unit quaternions (representing rotations), their sum is generally  not  a unit quaternion and thus does not directly represent a simple rotation. It may need to be normalized if a unit quaternion is desired from the sum (e.g., in some averaging or interpolation schemes). 
#### Return
A new  Quat  representing the sum of this quaternion and  other . 
#### Parameters
other 
The  Quat  to add to this quaternion.