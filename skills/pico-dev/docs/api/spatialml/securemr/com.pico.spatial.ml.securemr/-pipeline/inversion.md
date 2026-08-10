# inversion | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / inversion 
# inversion
```kotlin
fun inversion(source: Tensor, result: Tensor)
```
Compute the matrix inversion. 
#### Parameters
source 
the matrix to be inverted. It must be a multi-dimensional tensor of 2 dimensions, whose datatype must either be a non-pixel datatype, or a RED-channel-only pixel type. 
result 
the required result to store the matrix inversion. It must also be a multi-dimensional tensor of 2 dimensions. It dimensions must be the same as those of  source . Its data type must be the same as that of  source . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.