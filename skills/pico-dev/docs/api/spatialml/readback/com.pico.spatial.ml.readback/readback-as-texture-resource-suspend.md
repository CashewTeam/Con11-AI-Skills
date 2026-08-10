# readbackAsTextureResourceSuspend | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / readbackAsTextureResourceSuspend 
# readbackAsTextureResourceSuspend
```kotlin
@RequiresApi(value = 27)
```suspend  fun  GlobalTensor . readbackAsTextureResourceSuspend ( ) :  TextureResource 
The suspend version of  readbackAsTextureResource . 
#### Return
Dynamic texture resource from the tensor. 
#### Throws
Spatial MLException 
if the application does not have the required permission(s), or if the  GlobalTensor  is invalid, or cannot be read back, such as a tensor created with  Tensor.SceneGraphInitInfo  config.