# Scale3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.geometry / Scale3D 
# Scale3D
```kotlin
@Stable
```class  Scale3D ( val  scaleX :  Float ,  val  scaleY :  Float ,  val  scaleZ :  Float ,  val  pivot :  NormalizedPoint3D  =  NormalizedPoint3D.Center ) 
Holds the values used to scale a 3D object 
Members 
## Constructors
Scale3D 
```kotlin
constructor(scaleX: Float, scaleY: Float, scaleZ: Float, pivot: NormalizedPoint3D = NormalizedPoint3D.Center)
```
## Types
Companion 
```kotlin
object Companion
```
companion object 
## Properties
pivot 
```kotlin
val pivot: NormalizedPoint3D
```
The pivot point to scale around. Default is  NormalizedPoint3D.Center 
scale X 
```kotlin
val scaleX: Float
```
The scale factor to apply on the X axis 
scale Y 
```kotlin
val scaleY: Float
```
The scale factor to apply on the Y axis 
scale Z 
```kotlin
val scaleZ: Float
```
The scale factor to apply on the Z axis 
## Functions
copy 
```kotlin
fun copy(scaleX: Float = this.scaleX, scaleY: Float = this.scaleY, scaleZ: Float = this.scaleZ, pivot: NormalizedPoint3D = this.pivot): Scale3D
```
Copy this scale 3D with new values 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```