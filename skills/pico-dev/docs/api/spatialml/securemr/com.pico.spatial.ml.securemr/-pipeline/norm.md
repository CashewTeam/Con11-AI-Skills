# norm | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / norm 
# norm
```kotlin
fun norm(type: Pipeline.NormType, srcTensor: Tensor, result: Tensor)
```
Compute the norm of a tensor. 
#### Parameters
type 
type of the norm. 
src Tensor 
the tensor whose norm will be computed. It must be a multi-dimensional tensor of exact 2 dimensions. 
result 
the required result, to store the norm value. It must contain a single value. e.g., if it is a multi-dimensional tensor, it must be of 1 channel, with dimensions like 1x1x...; or if it is a scalar array tensor, it must be of size 1. It cannot be a scene-graph tensor. The data type must be 32-/64-bit float.