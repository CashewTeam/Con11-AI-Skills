# ModelNodeEncoding | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / ModelNodeEncoding / ModelNodeEncoding 
# ModelNodeEncoding
```kotlin
constructor(nodeName: String, tensor: Tensor)
```
#### Parameters
node Name 
the name string in the model computation graph. 
tensor 
the tensor to be associated with the computation graph node. The tensor must be of the same number of values as the node's requirement in the computation graph. The tensor must be a multi-dimensional one.