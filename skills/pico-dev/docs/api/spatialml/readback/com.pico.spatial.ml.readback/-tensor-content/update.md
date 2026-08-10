# update | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / TensorContent / update 
# update
```kotlin
fun update()
```
Update to the tensor's up-to-date's content. If you have changed the content, but have not call the  applyChange  or  applyChangeSuspend  to write the updated content back to the tensor, the change will be discarded. 
Calling the method has the same requirement as  readbackContent : the application must have necessary permissions being granted by users. 
This method  may  block your calling thread for a while to wait for the running pipelines which are currently writing to the  GlobalTensor  to finish. On return, the method take a snapshot of the tensor's content at that moment. If any pipeline in SpatialML framework change the tensor's content afterwards, the data in this  TensorContent  will be updated until the  update  is manually called. 
#### See also
readback Content 
#### Throws
Spatial MLException 
if it fails to read back latest content from the same tensor. Possible reasons are:     1. The application does not have the necessary permissions any more,     1. The SpatialML framework encounters internal error to perform the request, such as no        enough memory to allocate for snapshotting the tensor's content.