# asShortArray | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / TensorContent / Slice / asShortArray 
# asShortArray
```kotlin
fun asShortArray(): ShortArray
```
Ready the selected range from the tensor as  Short s. The tensor must be a of  Tensor.DataType.INT16 , otherwise you cannot read its content as  ShortArray . 
#### Return
the selected range of the tensor content as integer array. 
#### Throws
Spatial MLException 
if the tensor's datatype is not  Tensor.DataType.INT16 .