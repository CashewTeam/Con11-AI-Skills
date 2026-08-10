# com.pico.spatial.ui.foundation.effect3d | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.effect3d 
# Package-level declarations
Functions 
## Functions
rotate3D 
```kotlin
fun Modifier.rotate3D(block: () -> Rotation3D): Modifier
```
Rotates the composable around the given  Rotation3D 
```kotlin
fun Modifier.rotate3D(degree: Float, axis: RotationAxis3D, pivot: NormalizedPoint3D = NormalizedPoint3D.Center): Modifier
```
Rotates the composable around the given  axis  and  pivot  by  degree 
scale3D 
```kotlin
fun Modifier.scale3D(block: () -> Scale3D): Modifier
```
Scales the composable by the given  Scale3D  factors, around the given pivot point. 
```kotlin
fun Modifier.scale3D(scale: Float, pivot: NormalizedPoint3D = NormalizedPoint3D.Center): Modifier
```
Scales the composable by the given  scale  factor, around the given  pivot  point. 
```kotlin
fun Modifier.scale3D(scaleX: Float, scaleY: Float, scaleZ: Float, pivot: NormalizedPoint3D = NormalizedPoint3D.Center): Modifier
```
Scales the composable by the given  scaleX ,  scaleY  and  scaleZ  factors, around the given  pivot  point.