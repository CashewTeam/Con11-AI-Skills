# unaryMinus | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / unaryMinus 
# unaryMinus
```kotlin
operator fun unaryMinus(): Quat
```
Overloads the unary minus operator ( - ) to perform component-wise negation of this quaternion. 
Each component ( x ,  y ,  z , and  w ) of this quaternion is negated. 
Note: For unit quaternions representing rotations,  -q  represents the exact same rotation as  q . This operation does not compute the quaternion conjugate or inverse for rotation purposes (unless it's a specific case like a pure vector quaternion). 
#### Return
A new  Quat  representing the component-wise negation of this quaternion.