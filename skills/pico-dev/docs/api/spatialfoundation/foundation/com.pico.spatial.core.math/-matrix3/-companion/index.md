# Companion | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix3 / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  Matrix3 . 
Members 
## Functions
from Float Array 
```kotlin
@JvmStatic
```fun  fromFloatArray ( array :  FloatArray ) :  Matrix3 
Creates a new  Matrix3  instance from a float array. 
identity 
```kotlin
@JvmStatic
```fun  identity ( ) :  Matrix3 
Gets the identity of the  Matrix3  instance. 
rotate By Degrees 
```kotlin
@JvmStatic
```fun  rotateByDegrees ( angleInDegrees :  Float ) :  Matrix3 
Creates and returns a 3x3 matrix representing a 2D rotation in the XY-plane (equivalent to a rotation around the Z-axis in a 3D context). 
scale 
```kotlin
@JvmStatic
```fun  scale ( x :  Float ,  y :  Float ) :  Matrix3 
Creates and returns a 3x3 scaling matrix for 2D scaling operations, with scaling factors applied along the X and Y axes. The Z-axis scaling factor is implicitly set to  1.0f . 
translate 
```kotlin
@JvmStatic
```fun  translate ( x :  Float ,  y :  Float ) :  Matrix3 
Creates and returns a 3x3 matrix representing a 2D translation by  x  along the X-axis and  y  along the Y-axis.