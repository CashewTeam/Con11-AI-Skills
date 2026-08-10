# rectifiedVSTAccess | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / rectifiedVSTAccess 
# rectifiedVSTAccess
```kotlin
fun rectifiedVSTAccess(rightImageResult: Tensor?, leftImageResult: Tensor?, timestampResult: Tensor?, cameraMatrixResult: Tensor?)
```
Obtain the latest camera images. The images will be rectified internal against len distortion. 
#### Parameters
right Image Result 
an optional result, to store the right-eye image from the camera. If provided, it must be a multi-dimensions image tensor of  DataType.Image.R8G8B8_U  or  DataType.Image.R8G8B8A8_U  pixel type. We recommend its height and width match the  imageHeight  and  imageWidth  fields of  SpatialMLSession.InitInfo  when the session is created, to avoid overhead for additional scaling. 
left Image Result 
an optional result, to store the right-eye image from the camera. If provided, it must be a multi-dimensions image tensor of  DataType.Image.R8G8B8_U  or  DataType.Image.R8G8B8A8_U  pixel type. We recommend its height and width match the  imageHeight  and  imageWidth  fields of  SpatialMLSession.InitInfo  when the session is created, to avoid overhead for additional scaling. 
timestamp Result 
an optional result, to store the camera timestamp when the images are exposed. You will find this result useful when estimates the depths of the points on the images, or compute the transform between the camera space and the world space. 
camera Matrix Result 
an optional result, to store the camera intrinsic matrix. If provided, it must be a multi-dimension tensor, with dimensions = 3x3. Its datatype must be  DataType.FLOAT64 ,  DataType.FLOAT32 ,  DataType.Image.R_FLOAT , or  DataType.Image.R_DOUBLE . 
#### See also
Pipeline. uv To3DIn Camera Space