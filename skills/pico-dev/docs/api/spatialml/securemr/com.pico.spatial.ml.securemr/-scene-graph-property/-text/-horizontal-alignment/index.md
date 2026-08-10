# HorizontalAlignment | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / Text / HorizontalAlignment 
# HorizontalAlignment
```kotlin
object HorizontalAlignment : SceneGraphProperty.Text
```
Update horizontal alignment of text. 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be a single scalar value of  Tensor.DataType.UINT8  datatype, i.e. the tensor must be 
- 
A multi-dimensional tensor of non-pixel datatype, or RED-channel-only pixel type, and     all dimensions equal 1, or 
- 
A scalar array of size 1. 
If the scalar contained by the tensor is  0 , the horizontal alignment is left-aligned. If the scalar contained by the tensor is  1 , the horizontal alignment is center-aligned. If the scalar contained by the tensor is  2 , the horizontal alignment is right-aligned. If the scalar contained by the tensor is  3 , the horizontal alignment is justified- aligned, in which case spaces between words are adjusted to align both left and right edges with the container. If the scalar contained by the tensor is  4 , the horizontal alignment is flush- aligned, in which case spaces between  all characters  are adjusted to align both left and right edges with the container. 
Pipeline.TextHorizontalAlignment  and  Pipeline.updateSceneGraphTextHorizontalAlignment  provide convenient interface for you to directly update the text component alignment, without needing to manually create the tensors and set the values. 
#### See also
Pipeline. Text Horizontal Alignment