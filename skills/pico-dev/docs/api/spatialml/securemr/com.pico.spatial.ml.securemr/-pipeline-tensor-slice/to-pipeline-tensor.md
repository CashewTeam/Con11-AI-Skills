# toPipelineTensor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / PipelineTensorSlice / toPipelineTensor 
# toPipelineTensor
```kotlin
fun toPipelineTensor(config: Tensor.InitInfo): PipelineTensor
```
A convenient way to copy elements from a slice to an intermedia tensor, to be used by other pipeline method. 
#### Return
the tensor whose content will be the copy of the slice. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.