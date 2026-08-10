# bitwiseOr | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / bitwiseOr 
# bitwiseOr
```kotlin
fun bitwiseOr(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an bitwise-or of two input tensors. 
#### Parameters
tensor1 
one input tensor. It cannot be a scene graph tensor. 
tensor2 
another input tensor, which must be of the same usage, number of channels, data type, and sizes or dimensions as  tensor1 , i.e.,  tensor1  and  tensor2  must have exactly the same  Tensor.InitInfo  when created. 
result 
the tensor to hold the bitwise-or of  tensor1  and  tensor2 . The usage, number of channel, data type, and sizes or dimensions must be the same as those of  tensor1  and  tensor2 , i.e.,  result  must be created with the same  Tensor.InitInfo  as  tensor1  and  tensor2 . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.