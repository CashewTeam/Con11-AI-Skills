# readbackContentSuspend | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / readbackContentSuspend 
# readbackContentSuspend
```kotlin
@RequiresApi(value = 27)
```suspend  fun  GlobalTensor . readbackContentSuspend ( ) :  TensorContent 
Suspend version of  readbackContent  because the readback may block the calling thread. 
#### Return
Tensor content read from the  GlobalTensor . 
#### See also
readback Content 
#### Throws
Spatial MLException 
if the application does not have the required permission(s), or if the  GlobalTensor  is invalid, or cannot be read back, such as a tensor created with  Tensor.SceneGraphInitInfo  config.