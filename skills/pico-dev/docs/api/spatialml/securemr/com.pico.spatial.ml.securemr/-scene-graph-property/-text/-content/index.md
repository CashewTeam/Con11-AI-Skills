# Content | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / Text / Content 
# Content
```kotlin
object Content : SceneGraphProperty.Text
```
Update the content of the text component. 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter can be any tensor. 
- 
If the tensor is a string tensor, i.e., created by  Tensor.StringInitInfo  (or a     created by Tensor.ScalarInitInfo with  datatype  being Tensor.DataType.INT8 or     Tensor.DataType.UINT8) the tensor will be interpreted as a UTF-8 string, as the text     content directly. 
- 
Otherwise, the tensor's values will be converted to text one by one and concatenated     into a single string as the text content.