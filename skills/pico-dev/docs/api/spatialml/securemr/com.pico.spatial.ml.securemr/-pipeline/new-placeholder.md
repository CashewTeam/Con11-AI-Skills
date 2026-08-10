# newPlaceholder | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / newPlaceholder 
# newPlaceholder
```kotlin
fun newPlaceholder(config: Tensor.InitInfo): PipelineTensorPlaceholder
```
Create a new placeholder tensor inside this pipeline. Different from a local tensor, a placeholder tensor has  no  local memory allocated in the pipeline's scope; on the contrary, the placeholder must refer to a compatible global tensor when the pipeline is submitted for execution. 
#### Return
the newly created placeholder, whose lifecycle is bound to this pipeline. 
#### Parameters
config 
the configuration of the placeholder. The placeholder is  only  compatible with the global tensor having  the same  configuration. 
#### See also
Pipeline Tensor Placeholder 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.