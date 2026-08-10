# times | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / times 
# times
```kotlin
operator fun times(other: Quat): Quat
```
Times two  Quat  instances. 
#### Return
The new  Quat  instance, the result of this  Quat  instance timing another  Quat  instance. 
#### Parameters
other 
Another  Quat  instance that will be timed. 
```kotlin
operator fun times(scalar: Float): Quat
```
Overloads the  *  operator to perform multiplication of this quaternion by a scalar value. 
Each component ( x ,  y ,  z , and  w ) of this quaternion is multiplied by the  scalar . 
Note: If this quaternion represents a rotation (i.e., it is a unit quaternion), multiplying by a scalar other than  1.0  or  -1.0  will result in a quaternion that no longer has unit length and thus may not represent a pure rotation directly. 
#### Return
A new  Quat  representing the result of the scalar multiplication. 
#### Parameters
scalar 
The scalar  Float  value to multiply this quaternion by.