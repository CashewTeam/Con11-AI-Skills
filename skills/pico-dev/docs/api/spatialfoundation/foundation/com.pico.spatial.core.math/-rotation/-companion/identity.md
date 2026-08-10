# identity | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Rotation / Companion / identity 
# identity
```kotlin
@JvmStatic
```fun  identity ( ) :  Rotation 
Gets the identity rotation, which represents no rotation. 
This is a unit quaternion where the scalar part  w  is 1 and the vector part  (x, y, z)  is zero. Applying this rotation to any vector or object will result in no change. It is useful as a default value or for initializing a rotation. 
#### Return
The identity  Rotation  instance.