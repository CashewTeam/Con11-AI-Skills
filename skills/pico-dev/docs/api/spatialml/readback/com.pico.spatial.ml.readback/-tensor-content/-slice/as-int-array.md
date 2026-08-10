# asIntArray | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / TensorContent / Slice / asIntArray 
# asIntArray
```kotlin
fun asIntArray(): IntArray
```
Ready the selected range from the tensor as integers. The tensor must be a of  Tensor.DataType.INT32 , otherwise you cannot read its content as  IntArray . 
#### Return
the selected range of the tensor content as integer array. 
#### Throws
Spatial MLException 
if the tensor's datatype is not  Tensor.DataType.INT32 .