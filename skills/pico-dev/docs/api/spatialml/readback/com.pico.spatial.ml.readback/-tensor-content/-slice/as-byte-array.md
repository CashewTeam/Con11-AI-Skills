# asByteArray | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / TensorContent / Slice / asByteArray 
# asByteArray
```kotlin
fun asByteArray(): ByteArray
```
Ready the selected range from the tensor as  Byte s. The tensor must be a of  Tensor.DataType.INT8 , otherwise you cannot read its content as  ByteArray . 
#### Return
the selected range of the tensor content as integer array. 
#### Throws
Spatial MLException 
if the tensor's datatype is not  Tensor.DataType.INT8 .