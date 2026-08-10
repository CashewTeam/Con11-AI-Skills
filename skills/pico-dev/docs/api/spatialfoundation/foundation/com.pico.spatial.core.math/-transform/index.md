# Transform | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Transform 
# Transform
```kotlin
class Transform
```
Represents a transform. 
Members 
## Constructors
Transform 
```kotlin
constructor()
```
Creates a  Transform  instance with position, rotation (as  EulerAngles ), and scale. This is the default  Transform  constructor. 
```kotlin
constructor(position: Vector3, rotation: EulerAngles, scale: Vector3)
```
Creates a  Transform  instance with specified position, rotation (as  EulerAngles ), and scale. 
```kotlin
constructor(position: Vector3, rotation: Quat, scale: Vector3)
```
Creates a  Transform  instance with specified position, rotation (as Quat), and scale. 
## Properties
position 
```kotlin
val position: Vector3
```
The position vector of the transform. 
quaternion 
```kotlin
val quaternion: Quat
```
The rotation represented as a quaternion. 
rotation 
```kotlin
val rotation: EulerAngles
```
The rotation represented as an  EulerAngles . 
scale 
```kotlin
val scale: Vector3
```
The scale vector of the transform. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```rotate 
```kotlin
fun rotate(rotation: Quat): Transform
```
Applies an additional rotation to this transform's current orientation and returns a new  Transform  with the combined rotation. 
scale 
```kotlin
fun scale(scale: Vector3): Transform
```
Applies an additional scaling to this transform's current scale and returns a new  Transform  with the combined scale. 
to Float Array 
```kotlin
fun toFloatArray(): FloatArray
```
Converts the  Transform  instance to a float array. 
to Matrix4 
```kotlin
fun toMatrix4(): Matrix4
```
Reconstructs a 4x4 transformation matrix from this Transform's position, quaternion, and scale components. 
to String 
```kotlin
open override fun toString(): String
```translate 
```kotlin
fun translate(translation: Vector3): Transform
```
Applies an additional translation to this transform's current position and returns a new  Transform  with the combined position.