# RotationAxis3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.geometry / RotationAxis3D 
# RotationAxis3D
```kotlin
@Stable
```class  RotationAxis3D ( val  x :  Float  =  0.0f ,  val  y :  Float  =  0.0f ,  val  z :  Float  =  0.0f ) 
Presents a 3d axis 
Members Members & Extensions 
## Constructors
Rotation Axis3D 
```kotlin
constructor(x: Float = 0.0f, y: Float = 0.0f, z: Float = 0.0f)
```
## Types
Companion 
```kotlin
object Companion
```
Holds built-in  RotationAxis3D  instances 
## Properties
x 
```kotlin
val x: Float
```
x-axis value 
y 
```kotlin
val y: Float
```
y-axis value 
z 
```kotlin
val z: Float
```
z-axis value 
## Functions
copy 
```kotlin
fun copy(x: Float = this.x, y: Float = this.y, z: Float = this.z): RotationAxis3D
```
Returns a copy of this instance optionally overriding the x, y or z parameter 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```to Vector3 
```kotlin
fun RotationAxis3D.toVector3(): Vector3
```
RotationAxis3D  convert to  Vector3 
unary Minus 
```kotlin
operator fun unaryMinus(): RotationAxis3D
```
Negates the rotation axis.