# bytewiseAny | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / bytewiseAny 
# bytewiseAny
```kotlin
fun bytewiseAny(operand: Tensor, result: Tensor)
```
Perform a byte-wise any on all the values constituting the tensor. 
#### Parameters
operand 
the tensor as input. 
result 
the tensor must have one value only. The value will be written as zero if the any operation produces "false", i.e., all bytes are zeros. Otherwise, if any bytes of the  operand  are non-zero, the  result  is evaluated as "true" so the value of the  result  tensor will be written as non-zero. Additionally, the data type of the result must be of integral types. The  result  tensor cannot be a scene graph tensor. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.