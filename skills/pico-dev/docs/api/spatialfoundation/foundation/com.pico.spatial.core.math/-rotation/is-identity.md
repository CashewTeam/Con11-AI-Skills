# isIdentity | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Rotation / isIdentity 
# isIdentity
```kotlin
val isIdentity: Boolean
```
A boolean value that indicates whether this rotation is effectively an identity rotation (no rotation). Checks if the scalar part  w  of the internal quaternion is close to +/-1 and the vector part  (x,y,z)  is close to zero, within  EPSILON(1e-6f)  and  EPSILON_SQ(1e-12f)  tolerances.