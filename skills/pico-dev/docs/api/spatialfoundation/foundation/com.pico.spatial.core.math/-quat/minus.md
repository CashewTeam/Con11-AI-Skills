# minus | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / minus 
# minus
```kotlin
operator fun minus(other: Quat): Quat
```
Overloads the  -  operator to perform component-wise subtraction of another quaternion ( other ) from this quaternion ( this ). 
Each component ( x ,  y ,  z , and  w ) of the resulting quaternion is the difference between the corresponding components of this quaternion and the  other  quaternion ( this_component - other_component ). 
Note: If both input quaternions are unit quaternions (representing rotations), their difference is generally  not  a unit quaternion and thus does not directly represent a simple rotation. 
#### Return
A new  Quat  representing the difference ( this  -  other ). 
#### Parameters
other 
The  Quat  to subtract from this quaternion.