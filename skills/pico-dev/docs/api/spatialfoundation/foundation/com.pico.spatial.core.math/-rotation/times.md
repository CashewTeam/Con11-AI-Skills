# times | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Rotation / times 
# times
```kotlin
operator fun times(other: Rotation): Rotation
```
Combines this rotation with another rotation  other . The result  this * other  represents applying the rotation  other  first, then applying  this  rotation. The resulting quaternion is normalized to counteract potential floating-point drift. 
#### Return
A new  Rotation  representing the combined rotation. 
#### Parameters
other 
The  Rotation  to multiply this rotation by.