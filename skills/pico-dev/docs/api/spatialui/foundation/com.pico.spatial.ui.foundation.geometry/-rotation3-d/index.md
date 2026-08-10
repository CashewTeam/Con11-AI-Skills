# Rotation3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.geometry / Rotation3D 
# Rotation3D
```kotlin
@Stable
```class  Rotation3D ( val  degree :  Float ,  val  axis :  RotationAxis3D ,  val  pivot :  NormalizedPoint3D  =  NormalizedPoint3D.Center ) 
Holds the values used by 3d rotation 
Members 
## Constructors
Rotation3D 
```kotlin
constructor(degree: Float, axis: RotationAxis3D, pivot: NormalizedPoint3D = NormalizedPoint3D.Center)
```
## Types
Companion 
```kotlin
object Companion
```
Holds built-in  Rotation3D  instances 
## Properties
axis 
```kotlin
val axis: RotationAxis3D
```
The axis of rotation, see  RotationAxis3D 
degree 
```kotlin
val degree: Float
```
The degree by which to rotate the composable 
pivot 
```kotlin
val pivot: NormalizedPoint3D
```
The  NormalizedPoint3D  relative the composable about which to perform the rotation 
## Functions
copy 
```kotlin
fun copy(degree: Float = this.degree, axis: RotationAxis3D = this.axis, pivot: NormalizedPoint3D = this.pivot): Rotation3D
```
Returns a copy of this instance optionally overriding the degree, axis or pivot parameter 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```rotate By 
```kotlin
fun rotateBy(quat: Quat): Rotation3D
```
Rotate this  Rotation3D  by  quat 
```kotlin
fun rotateBy(rotation: Rotation3D): Rotation3D
```
Rotate this  Rotation3D  by  rotation 
to Quaternion 
```kotlin
fun toQuaternion(): Quat
```
Rotation3D  convert to  Quat 
to String 
```kotlin
open override fun toString(): String
```