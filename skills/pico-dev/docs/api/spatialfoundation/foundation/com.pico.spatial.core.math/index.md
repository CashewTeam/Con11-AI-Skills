# com.pico.spatial.core.math | PICO Spatial SDK

foundation / com.pico.spatial.core.math 
# Package-level declarations
Types 
## Types
Bool3 
```kotlin
class Bool3
```
Represents a structure containing three boolean values. 
Color3 
```kotlin
class Color3
```
Represents a gamma color with red, green, blue components. Component values are typically in the range 0, 1, though this is not strictly enforced. 
Color4 
```kotlin
class Color4
```
Represents a gamma color with red, green, blue, and alpha components. Component values are typically in the range 0, 1, though this is not strictly enforced. 
Euler Angles 
```kotlin
class EulerAngles(val pitch: Float = 0.0f, val yaw: Float = 0.0f, val roll: Float = 0.0f)
```
Represents a rotation in 3D space using euler angles. 
Matrix3 
```kotlin
class Matrix3(val m00: Float, val m01: Float, val m02: Float, val m10: Float, val m11: Float, val m12: Float, val m20: Float, val m21: Float, val m22: Float)
```
Represents a 3x3 matrix. 
Matrix4 
```kotlin
class Matrix4(val m00: Float, val m01: Float, val m02: Float, val m03: Float, val m10: Float, val m11: Float, val m12: Float, val m13: Float, val m20: Float, val m21: Float, val m22: Float, val m23: Float, val m30: Float, val m31: Float, val m32: Float, val m33: Float)
```
Represents a 4x4 matrix. 
Quat 
```kotlin
class Quat
```
Represents a quaternion. 
Rotation 
```kotlin
class Rotation(quat: Quat)
```
Represents a rotation in three-dimensional space. 
Transform 
```kotlin
class Transform
```
Represents a transform. 
Vector2 
```kotlin
class Vector2
```
Represents a vector2. 
Vector3 
```kotlin
class Vector3
```
Represents a vector3. 
Vector4 
```kotlin
class Vector4
```
Represents a Vector4.