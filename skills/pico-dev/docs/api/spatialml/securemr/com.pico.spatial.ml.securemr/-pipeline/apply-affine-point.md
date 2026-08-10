# applyAffinePoint | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / applyAffinePoint 
# applyAffinePoint
```kotlin
fun applyAffinePoint(affineMatrix: Tensor, srcPoints: Tensor, affinedPoints: Tensor)
```
Apply the affine transform on 2D points rather than 2D images. 
#### Parameters
affine Matrix 
the affine matrix. The tensor must be a multi-dimension tensor with dimensions = 2x3. The data type must be 32-/64-bit float and cannot be a multi-channel- pixel datatype. You can use the result from  getAffine  operation here. 
src Points 
points to be transformed. The tensor must be a floating-point point2 array (i.e., created with  Tensor.Point2ArrayInitInfo ) of size  N , or a multi-dimensional tensor of  Tensor.DataType.Image.RG_FLOAT  or  Tensor.DataType.Image.RG_DOUBLE , with dimensions = 1x N  or  N x1. 
affined Points 
the required result, to store the affined points. The tensor must be a point2 array (i.e., created with  Tensor.Point2ArrayInitInfo ) of size  N , or a multi-dimensional tensor of 2 channels, with dimensions = 1x N  or  N x1. The data type must be 32-/64-bit float. The  N  must be the same as that of  srcPoints . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.