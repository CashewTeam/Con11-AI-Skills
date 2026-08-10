# smallerThan | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / smallerThan 
# smallerThan
```kotlin
fun smallerThan(tensor1: Tensor, tensor2: Tensor, result: Tensor)
```
Perform an elementwise-smaller-than comparison of two input tensors. 
#### Parameters
tensor1 
one input tensor. It cannot be a scene graph tensor. 
tensor2 
another input tensor, which must be of the same usage, number of channels, data type, and sizes or dimensions as  tensor1 , i.e.,  tensor1  and  tensor2  must have exactly the same  Tensor.InitInfo  when created. 
result 
the tensor to hold the elementwise comparison result of  tensor1  and  tensor2 . The usage, number of channel, and sizes or dimensions must be the same as those of  tensor1  and  tensor2 , i.e.,  result  must be created with the same  Tensor.InitInfo  as  tensor1  and  tensor2 , except the data type can be different. The data type of  result  must be one integral type. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.