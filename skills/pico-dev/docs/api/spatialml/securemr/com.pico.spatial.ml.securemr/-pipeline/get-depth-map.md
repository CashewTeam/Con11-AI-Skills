# getDepthMap | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / getDepthMap 
# getDepthMap
```kotlin
fun getDepthMap(depthMapResult: Tensor)
```
Using PICO's depth sensor to get the depth map. The depth map's FOV is fixed at 90 degrees vertically, 109 degrees horizontally. 
#### Parameters
depth Map Result 
the required result from this operation, to store the latest depth map. It must be a multi-dimensional tensor (i.e., created by  Tensor.MultiDimensionalInitInfo ) with exactly 2 dimensions. Its datatype must be  Tensor.DataType.FLOAT32  or  Tensor.DataType.FLOAT64 , because the result will be the depth values in meter, from the center of the PICO device. The datatype must not be any multi-channel pixel types. The raw output from the depth sensor is 128 in height by 160 in width. Hence, it is recommended to use a tensor of the same shape  (128, 160)  to store the result to avoid interpolation. If a tensor of different shape is given, the raw depth map will be linear interpolated to the tensor's shape. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.