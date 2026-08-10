# readbackContent | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / readbackContent 
# readbackContent
```kotlin
@RequiresApi(value = 27)
```fun  GlobalTensor . readbackContent ( ) :  TensorContent 
Read the content back from a  GlobalTensor  in SpatialML framework. This method  may  block your calling thread for a while to wait for the running pipelines which are currently writing to the  GlobalTensor  to finish. 
If the current SpatialML session to which the  GlobalTensor  belongs utilizes the see-through camera data in any of its pipelines, the application  must  have the Android camera permission granted by users. 
If the current SpatialML session to which the  GlobalTensor  belongs utilizes the spatial-data data in any of its pipelines, the application  must  have the PICO spatial data permission granted by users. 
Also note that call to this method will take a snapshot of the tensor's content at the moment the method returns. If any pipeline in SpatialML framework updates the tensor's content afterwards, the returned  TensorContent  will not be updated, unless you call  TensorContent.update . 
#### Return
Tensor content read from the  GlobalTensor . 
#### See also
readback Content Suspend 
#### Throws
Spatial MLException 
if the application does not have the required permission(s), or if the  GlobalTensor  is invalid, or cannot be read back, such as a tensor created with  Tensor.SceneGraphInitInfo  config.