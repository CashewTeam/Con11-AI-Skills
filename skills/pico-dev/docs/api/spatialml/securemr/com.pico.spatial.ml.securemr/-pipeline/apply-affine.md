# applyAffine | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / applyAffine 
# applyAffine
```kotlin
fun applyAffine(affineMatrix: Tensor, srcImage: Tensor, affinedImage: Tensor)
```
Apply the affine transform on 2D image. 
#### Parameters
affine Matrix 
the affine matrix. The tensor must be a multi-dimension tensor with dimensions = 2x3. The data type must be 32-/64-bit float and cannot be a multi-channel- pixel datatype. You can use the result from  getAffine  operation here. 
src Image 
the image input to be affined. The tensor must be a multi-dimensional tensor of 2 dimensions. No requirement on the data type. 
affined Image 
the affined result of  srcImage  by  affineMatrix . The tensor must be a multi-dimensional tensor as that of  srcImage . Its data type must be the same as that of  srcImage  as well. The tensor should have 2 dimensions. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.