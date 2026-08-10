# scale | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Matrix3 / Companion / scale 
# scale
```kotlin
@JvmStatic
```fun  scale ( x :  Float ,  y :  Float ) :  Matrix3 
Creates and returns a 3x3 scaling matrix for 2D scaling operations, with scaling factors applied along the X and Y axes. The Z-axis scaling factor is implicitly set to  1.0f . 
The resulting matrix will be: 

```
| x   0.0  0.0 || 0.0  y   0.0 || 0.0  0.0  1.0 |
```
#### Return
A new  Matrix3  instance representing the specified 2D scaling transformation (with Z-axis scale of 1.0). 
#### Parameters
x 
The scaling factor along the X-axis. 
y 
The scaling factor along the Y-axis.