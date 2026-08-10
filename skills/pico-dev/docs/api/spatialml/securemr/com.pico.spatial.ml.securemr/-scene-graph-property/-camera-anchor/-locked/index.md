# Locked | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SceneGraphProperty / CameraAnchor / Locked 
# Locked
```kotlin
object Locked : SceneGraphProperty.CameraAnchor
```
The  CameraAnchor.Locked  sets the camera anchor to be at the locked mode, which means, the world pose of the entity will be overridden to the pose specified by the provided matrix with respect to the camera coordinate space at that moment. The world pose of the entity will then be locked, regardless of head/camera movement and the SpatialML container movement. 
If this property is used as the  Pipeline.updateSceneGraphProperty 's  targetProperty  parameter, the  data  tensor parameter must be: a multi-dimensional tensor of 2 dimensions:  4x4 , with  datatype  declared as  Tensor.DataType.FLOAT32 ,  Tensor.DataType.FLOAT64 ,  Tensor.DataType.Image.R_FLOAT ,  Tensor.DataType.Image.R_FLOAT_DYNAMIC  or  Tensor.DataType.Image.R_DOUBLE . The tensor specifies the transform matrix corresponding to the camera at the moment the property is updated.