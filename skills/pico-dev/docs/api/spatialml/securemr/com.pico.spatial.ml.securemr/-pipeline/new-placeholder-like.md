# newPlaceholderLike | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / newPlaceholderLike 
# newPlaceholderLike
```kotlin
fun newPlaceholderLike(globalTensor: GlobalTensor): PipelineTensorPlaceholder
```
Create a new placeholder tensor inside this pipeline with guarantee compatibility with the a  GlobalTensor , i.e., the newly created placeholder share the same configuration with the  GlobalTensor .  Note:  a placeholder tensor has  no  local memory allocated in the pipeline's scope; on the contrary, the placeholder must refer to a compatible global tensor when the pipeline is submitted for execution. 
#### Return
the newly created placeholder, whose lifecycle is bound to this pipeline. 
#### Parameters
global Tensor 
the global tensor with which the newly created placeholder must be compatible with. 
#### See also
Pipeline Tensor Placeholder 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.