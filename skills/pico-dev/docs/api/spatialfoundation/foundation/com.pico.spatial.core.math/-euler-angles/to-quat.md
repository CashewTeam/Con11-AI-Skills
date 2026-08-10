# toQuat | PICO Spatial SDK

foundation / com.pico.spatial.core.math / EulerAngles / toQuat 
# toQuat
```kotlin
fun toQuat(): Quat
```
Converts this  EulerAngles  instance into its equivalent  Quat  (quaternion) representation. 
The conversion is based on the specific  extrinsic ZXY rotation order  that this class represents. This means the rotations are applied sequentially around fixed world axes: 
- 
First, a  Roll  around the  world Z-axis . 
- 
Second, a  Pitch  around the  world X-axis . 
- 
Finally, a  Yaw  around the  world Y-axis . 
The resulting quaternion represents the same final orientation as these Euler angles. 
#### Return
A unit  Quat  that represents the rotation.