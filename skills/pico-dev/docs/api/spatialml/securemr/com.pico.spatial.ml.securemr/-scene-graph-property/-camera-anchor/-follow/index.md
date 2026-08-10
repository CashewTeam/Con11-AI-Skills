# Follow | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / CameraAnchor / Follow 
# Follow
```kotlin
object Follow : SceneGraphProperty.CameraAnchor
```
The  CameraAnchor.Follow  sets the camera anchor to be at the following mode, which means, once the camera anchor is set, the world pose of the entity will always be updated so that its transform with respect to the camera coordinate space will always remain the same as the provided matrix. 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be: a multi-dimensional tensor of 2 dimensions:  4x4 , with  datatype  declared as  Tensor.DataType.FLOAT32 ,  Tensor.DataType.Image.R_FLOAT ,  Tensor.DataType.Image.R_FLOAT_DYNAMIC  or  Tensor.DataType.Image.R_DOUBLE . The tensor specifies the transform matrix corresponding to the camera.