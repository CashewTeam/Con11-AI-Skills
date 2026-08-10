# ModelNodeEncoding | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / ModelNodeEncoding 
# ModelNodeEncoding
```kotlin
class ModelNodeEncoding(val nodeName: String, val tensor: Tensor)
```
The association of a node in a model (TFLite, etc.) computation graph and a pipeline tensor. 
#### Parameters
node Name 
the name string in the model computation graph. 
tensor 
the tensor to be associated with the computation graph node. The tensor must be of the same number of values as the node's requirement in the computation graph. The tensor must be a multi-dimensional one. 
Members 
## Constructors
Model Node Encoding 
```kotlin
constructor(nodeName: String, tensor: Tensor)
```
## Properties
node Name 
```kotlin
val nodeName: String
```tensor 
```kotlin
val tensor: Tensor
```