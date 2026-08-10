# uvTo3DInCameraSpace | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / uvTo3DInCameraSpace 
# uvTo3DInCameraSpace
```kotlin
fun uvTo3DInCameraSpace(uv: Tensor, timestamp: Tensor, camMatrix: Tensor, leftImage: Tensor, rightImage: Tensor, point3Result: Tensor)
```
Using PICO's depth sensor and stereo view RGB images, estimate the 3D coordinates of 2D points on camera output. 
#### Parameters
uv 
the 2D coordinates of points, corresponding to one left-eye camera image. The tensor must be a point2 array, (i.e., created with  Tensor.Point2ArrayInitInfo ) of size  N . The data type must be  DataType.INT32 , where  (0, 0)  is top-left corner of the camera image, and the  (H, W)  is the bottom-right corner, where  H  and  W  are the resolutions of the  session , where the  SpatialMLSession  is initialized. 
timestamp 
the camera timestamp of the left-eye image to which the  uv  is corresponding. It must be a timestamp tensor output from  rectifiedVSTAccess . 
cam Matrix 
the camera intrinsic matrix of the left-eye image to which the  uv  is corresponding. It must be a multi-dimensional tensor of 1 channel, dimensions = 3x3 and its data type should be 32-/64-bit float. You can directly use the output from  rectifiedVSTAccess . 
left Image 
the raw left-eye camera image from  rectifiedVSTAccess . It must be the output associated with the  timestamp . It is used to enhance the depth sensor's output using parallax. 
right Image 
the raw right-eye camera image from  rectifiedVSTAccess . It must be the output associated with the  timestamp . It is used to enhance the depth sensor's output using parallax. 
point3Result 
the required result from this operation, to store the estimated 3D coordinates corresponding to the 2D points in  uv . It must be a point3 array, created with  Tensor.Point3ArrayInitInfo  of size  N , where  N  must match that of  uv , or a multi-dimensional tensor with dimensions =  N x3 and of non-pixel datatype or RED-channel- pixel datatype. Alternatively, it can also be a multi-dimensional tensor with dimensions =  N x1 or 1x N , and of 3-channel pixel datatype (R, G and B channels will store the X, Y and Z coordinates of a point). 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.