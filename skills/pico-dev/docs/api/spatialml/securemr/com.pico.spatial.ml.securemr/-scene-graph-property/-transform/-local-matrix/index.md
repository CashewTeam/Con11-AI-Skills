# LocalMatrix | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / Transform / LocalMatrix 
# LocalMatrix
```kotlin
object LocalMatrix : SceneGraphProperty.Transform
```
Update the local matrix property of one entity's transform. If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be: a multi-dimensional tensor of 2 dimensions:  4x4 , with  datatype  declared as  Tensor.DataType.FLOAT32 ,  Tensor.DataType.FLOAT64 ,  Tensor.DataType.Image.R_FLOAT ,  Tensor.DataType.Image.R_FLOAT_DYNAMIC  or  Tensor.DataType.Image.R_DOUBLE .