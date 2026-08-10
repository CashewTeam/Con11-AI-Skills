# asDoubleArray | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / TensorContent / Slice / asDoubleArray 
# asDoubleArray
```kotlin
fun asDoubleArray(): DoubleArray
```
Ready the selected range from the tensor as doubles. The tensor must be a of  Tensor.DataType.FLOAT64 , otherwise you cannot read its content as  DoubleArray . 
#### Return
the selected range of the tensor content as double array. 
#### Throws
Spatial MLException 
if the tensor's datatype is not  Tensor.DataType.FLOAT64 .