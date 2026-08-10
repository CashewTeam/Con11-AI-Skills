# GlobalTensor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / GlobalTensor 
# GlobalTensor
```kotlin
@RequiresApi(value = 27)
```class  GlobalTensor  :  Tensor ,  BaseHandle 
Global tensor means they do  not  depend on certain  Pipeline , so they can be created and deleted outside the lifecycle of any  Pipeline s. Instead, they are bound to the framework session. Additionally, they cannot be directly accessed from  Pipeline s. A  Pipeline  tries to access a  GlobalTensor  must first create a  PipelineTensorPlaceholder  with the same initialization config inside itself, and during each pipeline submission, map the  PipelineTensorPlaceholder  to the  GlobalTensor . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior. 
Members 
## Properties
destructor 
```kotlin
open override val destructor: BaseHandle.HandleDestructor
```
The  BaseHandle 's implementation's destructor. 
id 
```kotlin
val id: Long
```
The tensor's opaque ID in SpatialML framework. 
## Functions
reset Tensor Value 
```kotlin
protected open override fun resetTensorValue()
```
Callback when the tensor resource is reset