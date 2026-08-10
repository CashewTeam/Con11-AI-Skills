# solvePnP | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / solvePnP 
# solvePnP
```kotlin
fun solvePnP(objPoints: Tensor, imgPoints: Tensor, camMatrix: Tensor, rotationVecResult: Tensor? = null, translationVecResult: Tensor? = null)
```
Run the OpenCV solve PnP algorithm. Solve PnP reverses the camera projection procedure: given the projected result (2D points) of the vertices of a mesh, and the original 3D coordinates of the mesh vertices corresponding to the mesh's local space, inferring the most likely pose of the mesh corresponding to the camera space. 
#### Parameters
obj Points 
a tensor holding the 3D coordinates of  N  mesh vertices, all corresponding to the mesh's local space. The tensor must be an array of point3 (  Tensor.Point3ArrayInitInfo ) of size  N , or a multi-dimensional tensor of floating-point pixel with 3 channels (R, G and B channels of a pixel will be treated as the X, Y and Z coordinates of a point). 
img Points 
a tensor holding the projected 2D coordinates of  N  mesh vertices, all corresponding to the camera's projection plane. The tensor must be an array of point2 (  Tensor.Point2ArrayInitInfo ) of size  N , or a multi-dimensional tensor of floatint-point pixel with 2 channels (R and G channels of such a pixel will be treated as the X and Y coordinates of a point). 
cam Matrix 
a tensor holding the camera's intrinsic matrix. Hence, the tensor must be a multi-dimensional tensor of  DataType.FLOAT32  or  DataType.FLOAT64  with dimension = 3x3. You can use the camera matrix output from the  rectifiedVSTAccess  directly. 
rotation Vec Result 
an optional result, storing the rotation part of the inferred pose from Solve PnP algorithm. The rotation is expressed as a rotation vector. Hence, it must be a multi-dimensional tensor of dimensions = 1x3 or 3x1. Due to the limitation of OpenCV compatibility, the tensor, if provided, must be of data type  Tensor.DataType.FLOAT64 . 
translation Vec Result 
an optional result, storing the translation part of the inferred pose from Solve PnP algorithm. The rotation is expressed as a rotation vector. Hence, it must be a multi-dimensional tensor of dimensions = 1x3 or 3x1. Due to the limitation of OpenCV compatibility, the tensor, if provided, must be of data type  Tensor.DataType.FLOAT64 . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.