# PipelineTensorPlaceholder | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineTensorPlaceholder 
# PipelineTensorPlaceholder
```kotlin
@RequiresApi(value = 27)
```class  PipelineTensorPlaceholder  :  PipelineTensor 
The pipeline tensor with no local storage, but only a placeholder to refer to some global tensor. When a pipeline is submitted for execution, the  PipelineTensorPlaceholder  inside it will be  null  unless it is mapped to a  GlobalTensor  of  exactly  the same  config . In that case, any reads from the placeholder will become reads from the mapped  GlobalTensor , and writes to it will thus become writes to the mapped  GlobalTensor . We have an internal synchronization mechanism to schedule the pipeline executions, so that if a  GlobalTensor  is being written to, there will no other running pipelines trying to access (read/write) the same  GlobalTensor . 
#### See also
Pipeline. RunTask 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior. 
Members 
## Functions
reset Tensor Value 
```kotlin
protected open override fun resetTensorValue()
```
Callback when the tensor resource is reset