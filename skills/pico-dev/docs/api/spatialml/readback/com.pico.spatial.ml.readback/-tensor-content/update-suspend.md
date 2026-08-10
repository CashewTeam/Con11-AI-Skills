# updateSuspend | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / TensorContent / updateSuspend 
# updateSuspend
```kotlin
suspend fun updateSuspend()
```
Suspended version of  update . 
#### See also
Tensor Content. update 
#### Throws
Spatial MLException 
if it fails to read back latest content from the same tensor. Possible reasons are:     1. The application does not have the necessary permissions any more,     1. The SpatialML framework encounters internal error to perform the request, such as no        enough memory to allocate for snapshotting the tensor's content.