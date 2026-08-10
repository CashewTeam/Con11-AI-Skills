# Rotation | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / Transform / Rotation 
# Rotation
```kotlin
object Rotation : SceneGraphProperty.Transform
```
Update the rotation property of one entity's transform. If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be: 
- 
A multi-dimensional tensor of 2 dimensions:  1x3  or  3x1  of datatype      Tensor.DataType.FLOAT32 , Tensor.DataType.FLOAT64,     Tensor.DataType.Image.R_DOUBLE, Tensor.DataType.Image.R_FLOAT or     Tensor.DataType.Image.R_FLOAT.DYNAMIC, containing the rotation expressed as a     rotation vector. 
- 
A multi-dimensional tensor of 2 dimensions:  1x4  or  4x1  of datatype      Tensor.DataType.FLOAT32 , Tensor.DataType.FLOAT64,     Tensor.DataType.Image.R_DOUBLE, Tensor.DataType.Image.R_FLOAT or     Tensor.DataType.Image.R_FLOAT.DYNAMIC, containing the rotation expressed as a     quaternion. 
- 
A multi-dimensional tensor of 3-channel pixel type and all dimensions must be  1      where the RED channel of each pixel will be read as X component of the rotation     vector, GREEN channel as Y and BLUE channel as Z. The datatype must be     Tensor.DataType.Image.RGB_FLOAT or Tensor.DataType.Image.RGB_DOUBLE. 
- 
A multi-dimensional tensor of 4-channel pixel type and all dimensions must be  1      where the RED channel of each pixel will be read as X component of the quaternion,     GREEN channel as Y, BLUE channel as Z and ALPHA channel as W. The datatype must be     Tensor.DataType.Image.RGBA_FLOAT or Tensor.DataType.Image.RGBA_DOUBLE. 
- 
A Point3 array of size 1, with datatype  Tensor.DataType.FLOAT32  or     Tensor.DataType.FLOAT64, containing the rotation expressed as a rotation vector. 
- 
A float array or a double array of size 3, i.e., a tensor created using     Tensor.FloatArrayInitInfo or Tensor.DoubleArrayInitInfo, containing the rotation     expressed as a rotation vector. 
- 
A float array or a double array of size 4, i.e., a tensor created using     Tensor.FloatArrayInitInfo or Tensor.DoubleArrayInitInfo, containing the rotation     expressed as a quaternion.