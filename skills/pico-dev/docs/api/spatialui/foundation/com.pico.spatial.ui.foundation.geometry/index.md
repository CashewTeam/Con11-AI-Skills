# com.pico.spatial.ui.foundation.geometry | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.geometry 
# Package-level declarations
Types Functions 
## Types
Dp Offset3D 
```kotlin
@Immutable
```class  DpOffset3D ( val  x :  Dp ,  val  y :  Dp ,  val  z :  Dp ) 
Represent a 3D offset in  Dp . 
Int Offset3D 
```kotlin
@Immutable
```class  IntOffset3D ( val  x :  Int ,  val  y :  Int ,  val  z :  Int ) 
Represent a 3D offset in pixel. 
Normalized Point3D 
```kotlin
@Stable
```class  NormalizedPoint3D ( val  x :  Float ,  val  y :  Float ,  val  z :  Float ) 
A normalized 3D point in view's local coordinator space. For each dimension: 
Rotation3D 
```kotlin
@Stable
```class  Rotation3D ( val  degree :  Float ,  val  axis :  RotationAxis3D ,  val  pivot :  NormalizedPoint3D  =  NormalizedPoint3D.Center ) 
Holds the values used by 3d rotation 
Rotation Axis3D 
```kotlin
@Stable
```class  RotationAxis3D ( val  x :  Float  =  0.0f ,  val  y :  Float  =  0.0f ,  val  z :  Float  =  0.0f ) 
Presents a 3d axis 
Scale3D 
```kotlin
@Stable
```class  Scale3D ( val  scaleX :  Float ,  val  scaleY :  Float ,  val  scaleZ :  Float ,  val  pivot :  NormalizedPoint3D  =  NormalizedPoint3D.Center ) 
Holds the values used to scale a 3D object 
## Functions
to Int Offset3D 
```kotlin
fun DpOffset3D.toIntOffset3D(density: Density): IntOffset3D
```
Convert  DpOffset3D  to  IntOffset3D 
to Offset3D 
```kotlin
fun DpOffset3D.toOffset3D(density: Density): Offset3D
```
Convert  Offset3D  to  DpOffset3D 
to Rotation Axis3D 
```kotlin
fun Vector3.toRotationAxis3D(): RotationAxis3D
```
Vector3  convert to  RotationAxis3D 
to Vector3 
```kotlin
fun RotationAxis3D.toVector3(): Vector3
```
RotationAxis3D  convert to  Vector3