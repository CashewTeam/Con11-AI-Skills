# com.pico.spatial.ml.securemr | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr 
# Package-level declarations
Types 
## Types
Base Handle 
```kotlin
interface BaseHandle
```
The base for all top-level SpatialML handles. 
Global Tensor 
```kotlin
@RequiresApi(value = 27)
```class  GlobalTensor  :  Tensor ,  BaseHandle 
Global tensor means they do  not  depend on certain  Pipeline , so they can be created and deleted outside the lifecycle of any  Pipeline s. Instead, they are bound to the framework session. Additionally, they cannot be directly accessed from  Pipeline s. A  Pipeline  tries to access a  GlobalTensor  must first create a  PipelineTensorPlaceholder  with the same initialization config inside itself, and during each pipeline submission, map the  PipelineTensorPlaceholder  to the  GlobalTensor . 
Pipeline 
```kotlin
@RequiresApi(value = 27)
```class  Pipeline  :  BaseHandle 
SpatialML pipeline. 
Pipeline Arithmetic Scope 
```kotlin
@RequiresApi(value = 27)
```class  PipelineArithmeticScope 
The scope for arithmetic operations between  Tensor  in  Pipeline . 
Pipeline Tensor 
```kotlin
@RequiresApi(value = 27)
```abstract  class  PipelineTensor ( val  rootPipeline :  Pipeline ,  hasMemory :  Boolean ,  config :  Tensor.InitInfo )  :  Tensor 
A PipelineTensor is a tensor that is bound to a  Pipeline . It has the same lifecycle as the  Pipeline  it is subordinate to. Depending on whether it has local memory, it can categorized into two subclasses:  PipelineTensorLocal  or  PipelineTensorPlaceholder . The former has local memory allocated to it, while the latter has no underlying memory, and works as a run-time reference. 
Pipeline Tensor Local 
```kotlin
@RequiresApi(value = 27)
```class  PipelineTensorLocal  :  PipelineTensor 
Pipeline tensor with local memory. 
Pipeline Tensor Placeholder 
```kotlin
@RequiresApi(value = 27)
```class  PipelineTensorPlaceholder  :  PipelineTensor 
The pipeline tensor with no local storage, but only a placeholder to refer to some global tensor. When a pipeline is submitted for execution, the  PipelineTensorPlaceholder  inside it will be  null  unless it is mapped to a  GlobalTensor  of  exactly  the same  config . In that case, any reads from the placeholder will become reads from the mapped  GlobalTensor , and writes to it will thus become writes to the mapped  GlobalTensor . We have an internal synchronization mechanism to schedule the pipeline executions, so that if a  GlobalTensor  is being written to, there will no other running pipelines trying to access (read/write) the same  GlobalTensor . 
Pipeline Tensor Slice 
```kotlin
@RequiresApi(value = 27)
```class  PipelineTensorSlice ( originTensor :  PipelineTensor ,  sliceTensor :  PipelineTensor ) 
A wrapper of the pipeline tensor, with a slice onto this tensor. The slice must be a tensor of SLICE_ARRAY usage. 
Scene Graph Property 
```kotlin
sealed class SceneGraphProperty
```
Specifying the component and the field to be updated in  Pipeline.updateSceneGraphProperty . 
Spatial MLException 
```kotlin
class SpatialMLException(message: String?, cause: Throwable? = null) : Exception
```
The exception that SpatialML could throw. 
Spatial MLInstance 
```kotlin
@RequiresApi(value = 27)
```interface  SpatialMLInstance 
The interface of SpatialML instance. An  SpatialMLInstance  must be created before any SpatialML APIs or commands are executed. 
Spatial MLSession 
```kotlin
@RequiresApi(value = 27)
```class  SpatialMLSession  :  BaseHandle 
A handle to each session of SpatialML framework usage. For each session, a dedicated SpatialML container for securely rendering mixed-reality components will be allocated. 
Tensor 
```kotlin
@RequiresApi(value = 27)
```abstract  class  Tensor ( val  config :  Tensor.InitInfo ) 
Root class of all tensors (global and pipeline).