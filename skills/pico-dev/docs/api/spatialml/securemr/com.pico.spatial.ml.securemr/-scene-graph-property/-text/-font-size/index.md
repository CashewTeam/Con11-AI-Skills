# FontSize | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / Text / FontSize 
# FontSize
```kotlin
object FontSize : SceneGraphProperty.Text
```
Update the font size of text. 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be a single scalar value of  Tensor.DataType.FLOAT32  or  Tensor.DataType.FLOAT64  datatype, i.e. the tensor must be 
- 
A multi-dimensional tensor of non-pixel datatype or RED-channel-only pixel type, and     all dimensions equal 1, or 
- 
A scalar array of size 1.