# get | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / TensorContent / get 
# get
```kotlin
operator fun get(range: IntRange): TensorContent.Slice
```
Get a range of values from the tensor's content. The tensor must be of  Tensor.DataType.FLOAT64 ,  Tensor.DataType.FLOAT32 ,  Tensor.DataType.INT32 ,  Tensor.DataType.INT16  or  Tensor.DataType.INT8  datatypes. Otherwise, you may consider to directly use  buffer  to read the content byte-by-byte. 
#### Return
Slice of the tensor content. 
#### Parameters
range 
the indices of the range you want to read from the tensor's content. Note the indices should correspond to the datatype. For example, if you read back contents from a tensor of datatype  Tensor.DataType.INT32 ,  content[0..1].asIntArray()  will give you the first and the second integers, corresponding to the first  eight  bytes in  buffer . However, if the tensor's datatype is  Tensor.DataType.FLOAT64 ,  content[0..1].asDoubleArray()  will given you the first and the second doubles, which covers the first  sixteen  bytes in  buffer  instead. 
```kotlin
operator fun get(index: Int): Number
```
Get a value from the tensor's content by index. The tensor must be of  Tensor.DataType.FLOAT64 ,  Tensor.DataType.FLOAT32 ,  Tensor.DataType.INT32 ,  Tensor.DataType.INT16  or  Tensor.DataType.INT8  datatypes. Otherwise, you may consider to directly use  buffer  to read the content byte-by-byte. 
#### Return
The value at selected index. 
#### Parameters
index 
the index of the value you want to read from the tensor's content. Note the index should correspond to the datatype. 
For example, if you read back contents from a tensor of datatype  Tensor.DataType.INT32 ,  content[1].asIntArray()  will give you the second integer, corresponding to the  4~7  bytes in  buffer . 
However, if the tensor's datatype is  Tensor.DataType.FLOAT64 ,  content[1].asDoubleArray()  will given you the second double, which covers the  8~16  bytes in  buffer  instead. 
#### Throws
Spatial MLException 
if the tensor's datatype does not support its content to be read as numeric values from bytes, in which case you may consider to read from  buffer  directly.