# newGlobalTensor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / SpatialMLSession / newGlobalTensor 
# newGlobalTensor
```kotlin
fun newGlobalTensor(config: Tensor.InitInfo): GlobalTensor
```
Create new global tensors within the context of current framework session. 
#### Return
the newly created tensor. 
#### Parameters
config 
the Tensor's init info, as the configuration of the tensor. 
#### See also
Tensor Global Tensor 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounter internal error and cannot perform the requested behavior.