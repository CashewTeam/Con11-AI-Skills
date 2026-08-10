# Companion | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / Companion 
# Companion
```kotlin
object Companion
```
The companion object of  Matrix4 . 
Members 
## Functions
from Float Array 
```kotlin
@JvmStatic
```fun  fromFloatArray ( array :  FloatArray ) :  Matrix4 
Creates a new  Matrix4  instance from a float array. 
identity 
```kotlin
@JvmStatic
```fun  identity ( ) :  Matrix4 
Gets the identity of the  Matrix4  instance. 
look At 
```kotlin
@JvmStatic
```fun  lookAt ( eye :  Vector3 ,  target :  Vector3 ,  up :  Vector3 ) :  Matrix4 
Creates and returns a 4x4 view matrix that transforms coordinates from world space to camera (view) space. This is a standard "look-at" matrix, robustly handling common edge cases. 
ortho 
```kotlin
@JvmStatic
```fun  ortho ( left :  Float ,  right :  Float ,  bottom :  Float ,  top :  Float ,  near :  Float ,  far :  Float ) :  Matrix4 
Creates and returns a 4x4 orthographic projection matrix. 
perspective 
```kotlin
@JvmStatic
```fun  perspective ( fovYDegrees :  Float ,  aspectRatio :  Float ,  nearPlane :  Float ,  farPlane :  Float ) :  Matrix4 
Creates and returns a 4x4 perspective projection matrix. 
rotate By Degrees 
```kotlin
@JvmStatic
```fun  rotateByDegrees ( degrees :  Float ,  axis :  Vector3 ) :  Matrix4 
Creates and returns a 4x4 matrix representing a rotation around a given  axis  by an angle specified in  degrees . 
rotate XBy Degrees 
```kotlin
@JvmStatic
```fun  rotateXByDegrees ( degrees :  Float ) :  Matrix4 
Creates and returns a 4x4 matrix representing a rotation around the X-axis. The input angle is specified in  degrees . 
rotate YBy Degrees 
```kotlin
@JvmStatic
```fun  rotateYByDegrees ( degrees :  Float ) :  Matrix4 
Creates and returns a 4x4 matrix representing a rotation around the Y-axis. The input angle is specified in  degrees . 
rotate ZBy Degrees 
```kotlin
@JvmStatic
```fun  rotateZByDegrees ( degrees :  Float ) :  Matrix4 
Creates and returns a 4x4 matrix representing a rotation around the Z-axis. The input angle is specified in  degrees . 
rotation 
```kotlin
@JvmStatic
```fun  rotation ( eulerAngles :  EulerAngles ) :  Matrix4 
Creates and returns a 4x4 rotation matrix from the provided Euler angles (yaw, pitch, roll) specified in  degrees . 
scale 
```kotlin
@JvmStatic
```fun  scale ( scale :  Vector3 ) :  Matrix4 
Creates and returns a 4x4 matrix representing a 3D scaling transformation. 
translate 
```kotlin
@JvmStatic
```fun  translate ( translation :  Vector3 ) :  Matrix4 
Creates and returns a 4x4 matrix representing a 3D translation.