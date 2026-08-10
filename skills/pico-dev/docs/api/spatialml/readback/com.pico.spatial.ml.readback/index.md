# com.pico.spatial.ml.readback | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback 
# Package-level declarations
Types Functions 
## Types
Tensor Content 
```kotlin
@RequiresApi(value = 27)
```class  TensorContent  :  AutoCloseable 
Content read back from a  GlobalTensor . 
## Functions
readback As Texture Resource 
```kotlin
@RequiresApi(value = 27)
```fun  GlobalTensor . readbackAsTextureResource ( ) :  TextureResource 
If a  GlobalTensor  is a dynamic-texture one, you can use this method to read it back as a  TextureResource -compatible dynamic texture. You can use the dynamic texture as maps in your application's material, so that when the tensor's content is changed by SpatialML framework, the materials using the returned dynamic texture will all be updated automatically. 
readback As Texture Resource Suspend 
```kotlin
@RequiresApi(value = 27)
```suspend  fun  GlobalTensor . readbackAsTextureResourceSuspend ( ) :  TextureResource 
The suspend version of  readbackAsTextureResource . 
readback Content 
```kotlin
@RequiresApi(value = 27)
```fun  GlobalTensor . readbackContent ( ) :  TensorContent 
Read the content back from a  GlobalTensor  in SpatialML framework. This method  may  block your calling thread for a while to wait for the running pipelines which are currently writing to the  GlobalTensor  to finish. 
readback Content Suspend 
```kotlin
@RequiresApi(value = 27)
```suspend  fun  GlobalTensor . readbackContentSuspend ( ) :  TensorContent 
Suspend version of  readbackContent  because the readback may block the calling thread.