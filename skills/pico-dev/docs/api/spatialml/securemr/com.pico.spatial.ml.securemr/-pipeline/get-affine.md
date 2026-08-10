# getAffine | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / getAffine 
# getAffine
```kotlin
fun getAffine(srcPoints: Tensor, affinedPoints: Tensor, affineMatrixResult: Tensor)
```
Compute the 2D affine transform between two triangles. 
#### Parameters
src Points 
three points describing the triangle in the source planar space. The tensor must be a point2 array (i.e., created with  Tensor.Point2ArrayInitInfo ) of size 3, or a multi-dimensional tensor of 2-channel-pixel datatype, with dimensions = 1x3 or 3x1 (the RED and the GREEN channel of a pixel will be treated as the X and Y coordinates of a point). The data type must be 32-/64-bit float. 
affined Points 
three points describing the triangle in the affined planar space. The tensor must be a point2 array (i.e., created with  Tensor.Point2ArrayInitInfo ) of size 3, or a multi-dimensional tensor of 2-channel datatypes, with dimensions = 1x3 or 3x1 (the RED and the GREEN channel of a pixel will be treated as the X and Y coordinates of a point). The data type must be 32-/64-bit float. 
affine Matrix Result 
the required result, storing the affine matrix. The tensor must be a multi-dimension tensor with dimensions = 2x3. The data type must be  DataType.FLOAT32 ,  DataType.Image.R_FLOAT ,  DataType.Image.R_FLOAT_DYNAMIC , or  DataType.Image.R_DOUBLE . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.