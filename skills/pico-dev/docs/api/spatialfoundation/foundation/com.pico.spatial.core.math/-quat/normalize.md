# normalize | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Quat / normalize 
# normalize
```kotlin
fun normalize(): Quat
```
Returns a new quaternion with the same direction as this quaternion but with a length (magnitude) of 1.0. 
If this quaternion has a squared length less than 1e-12f (i.e., it is a zero or near-zero length quaternion), or if its components result in a non-finite squared length (NaN or Infinity), the original quaternion ( this ) is returned as it cannot be meaningfully normalized to a unit length. 
#### Return
A new  Quat  instance representing the normalized (unit length) quaternion, or  this  if normalization is not possible or meaningful.