# Companion | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Rotation / Companion 
# Companion
```kotlin
object Companion
```
Companion object providing utilities for rotation operations. 
Members 
## Types
Slerp Path 
```kotlin
enum SlerpPath : Enum<Rotation.Companion.SlerpPath>
```
Defines the arc path for Spherical Linear Interpolation (Slerp). 
## Functions
identity 
```kotlin
@JvmStatic
```fun  identity ( ) :  Rotation 
Gets the identity rotation, which represents no rotation. 
slerp 
```kotlin
@JvmStatic
```fun  slerp ( from :  Rotation ,  to :  Rotation ,  t :  Float ,  path :  Rotation.Companion.SlerpPath  =  SlerpPath.SHORTEST ) :  Rotation 
Performs Spherical Linear Interpolation (Slerp) between two rotations.