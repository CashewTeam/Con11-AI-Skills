# translate | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix3 / Companion / translate 
# translate
```kotlin
@JvmStatic
```fun  translate ( x :  Float ,  y :  Float ) :  Matrix3 
Creates and returns a 3x3 matrix representing a 2D translation by  x  along the X-axis and  y  along the Y-axis. 
This matrix is typically used for 2D affine transformations when points are represented in homogeneous coordinates (e.g.,  (px, py, 1) ). Applying this matrix to such a point results in  (px + x, py + y, 1) . 
The resulting matrix is: 

```
| 1.0  0.0  x   || 0.0  1.0  y   || 0.0  0.0  1.0 |
```
#### Return
A new  Matrix3  instance representing the specified 2D translation. 
#### Parameters
x 
The translation distance along the X-axis. 
y 
The translation distance along the Y-axis.