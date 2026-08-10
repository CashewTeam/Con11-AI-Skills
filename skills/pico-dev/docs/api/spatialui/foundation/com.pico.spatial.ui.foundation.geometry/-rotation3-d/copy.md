# copy | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.geometry / Rotation3D / copy 
# copy
```kotlin
fun copy(degree: Float = this.degree, axis: RotationAxis3D = this.axis, pivot: NormalizedPoint3D = this.pivot): Rotation3D
```
Returns a copy of this instance optionally overriding the degree, axis or pivot parameter 
#### Return
A new  Rotation3D  instance 
#### Parameters
degree 
The degree by which to rotate the composable 
axis 
The axis of rotation, see  RotationAxis3D 
pivot 
The  NormalizedPoint3D  relative the composable about which to perform the rotation