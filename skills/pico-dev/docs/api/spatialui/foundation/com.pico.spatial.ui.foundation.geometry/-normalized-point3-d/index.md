# NormalizedPoint3D | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.geometry / NormalizedPoint3D 
# NormalizedPoint3D
```kotlin
@Stable
```class  NormalizedPoint3D ( val  x :  Float ,  val  y :  Float ,  val  z :  Float ) 
A normalized 3D point in view's local coordinator space. For each dimension: 
- 
0 represents start of the dimension. 
- 
1 represents end of the dimension. 
For example, you can use 0.5 to represents center for each dimension. 
You also can use built-in values provides by SpatialUI like  Top 、 Center 、 Bottom  etc. 
A point outside the range 0,1 means a point outside of the view 
Members 
## Constructors
Normalized Point3D 
```kotlin
constructor(x: Float, y: Float, z: Float)
```
## Types
Companion 
```kotlin
object Companion
```
Holds built-in constant  NormalizedPoint3D  instances 
## Properties
x 
```kotlin
val x: Float
```
The normalized distance relative to origin point along x-axis. 
y 
```kotlin
val y: Float
```
The normalized distance relative to origin point along y-axis. 
z 
```kotlin
val z: Float
```
The normalized distance relative to origin point along z-axis. 
## Functions
copy 
```kotlin
fun copy(x: Float = this.x, y: Float = this.y, z: Float = this.z): NormalizedPoint3D
```
Returns a copy of this Point3D instance optionally overriding the x, y or z parameter 
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