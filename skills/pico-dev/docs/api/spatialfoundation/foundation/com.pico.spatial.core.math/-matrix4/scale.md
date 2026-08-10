# scale | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix4 / scale 
# scale
```kotlin
val scale: Vector3
```
Gets the apparent scaling factors along the local X, Y, and Z axes of the transformation represented by this matrix. 
This is determined by calculating the lengths (magnitudes) of the  right  (X-axis),  up  (Y-axis), and  forward  (Z-axis) basis vectors of this matrix. 
It provides accurate axial scaling factors if the matrix represents a transformation composed of rotations and/or uniform/non-uniform scaling  without any shear . 
If shear transformations are present in the matrix, the returned values will represent the lengths of the sheared basis vectors, which are influenced by both scaling and shearing, and may not purely represent the intended "scale" along the original axes. 
This property returns non-negative scale factors (i.e., the absolute magnitudes). It does not distinguish between positive and negative scaling (reflections). 
#### Return
A  Vector3  where  x  is  this.right.length() ,  y  is  this.up.length() , and  z  is  this.forward.length() .