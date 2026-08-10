# VerticalAlignment | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / Text / VerticalAlignment 
# VerticalAlignment
```kotlin
object VerticalAlignment : SceneGraphProperty.Text
```
Update vertical alignment of text. 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be a single scalar value of  Tensor.DataType.UINT8  datatype, i.e. the tensor must be 
- 
A multi-dimensional tensor of non-pixel datatype, or RED-channel-only pixel type, and     all dimensions equal 1, or 
- 
A scalar array of size 1. 
If the scalar contained by the tensor is  0 , the vertical alignment is top-aligned. If the scalar contained by the tensor is  1 , the horizontal alignment is center-aligned. If the scalar contained by the tensor is  2 , the horizontal alignment is bottom-aligned.