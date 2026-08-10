# PipelineTensorLocal | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineTensorLocal 
# PipelineTensorLocal
```kotlin
@RequiresApi(value = 27)
```class  PipelineTensorLocal  :  PipelineTensor 
Pipeline tensor with local memory. 
Note , due to synchronization limitation,  Tensor s of scene graph usage  cannot  be created as  PipelineTensorLocal . Instead, they must be initialized as  GlobalTensor , and have a  PipelineTensorPlaceholder  to refer to them during run time. 
Also, multi-dimensional  Tensor s with  dynamicTexture = true  cannot be created as  PipelineTensorLocal . Instead, they must be initialized as  GlobalTensor , and have a  PipelineTensorPlaceholder  to refer to them during run time. 
#### Parameters
root Pipeline 
the pipeline where the tensor is depending. 
config 
the pipeline tensor's initialization config. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior.