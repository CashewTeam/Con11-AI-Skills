# Position | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / Transform / Position 
# Position
```kotlin
object Position : SceneGraphProperty.Transform
```
Update the position property of one entity's transform. If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be: 
- 
A multi-dimensional tensor of 2 dimensions:  1x3  or  3x1  of datatype      Tensor.DataType.FLOAT32 , Tensor.DataType.FLOAT64,     Tensor.DataType.Image.R_DOUBLE, Tensor.DataType.Image.R_FLOAT or     Tensor.DataType.Image.R_FLOAT.DYNAMIC. 
- 
A multi-dimensional tensor of 3-channel pixel type and all dimensions must be  1      where the RED channel of each pixel will be read as X component of the vector, GREEN     channel as Y and BLUE channel as Z. The datatype must be     Tensor.DataType.Image.RGB_FLOAT or Tensor.DataType.Image.RGB_DOUBLE. 
- 
A Point3 array of size 1, with datatype  Tensor.DataType.FLOAT32  or     Tensor.DataType.FLOAT64 
- 
A float array or a double array of size 3, i.e., a tensor created using     Tensor.FloatArrayInitInfo or Tensor.DoubleArrayInitInfo.