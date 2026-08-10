# asFloatArray | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / TensorContent / Slice / asFloatArray 
# asFloatArray
```kotlin
fun asFloatArray(): FloatArray
```
Ready the selected range from the tensor as floats. The tensor must be a of  Tensor.DataType.FLOAT32 , otherwise you cannot read its content as  FloatArray . 
#### Return
the selected range of the tensor content as float array. 
#### Throws
Spatial MLException 
if the tensor's datatype is not  Tensor.DataType.FLOAT32 .