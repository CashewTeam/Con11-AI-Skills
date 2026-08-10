# TensorContent | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / TensorContent 
# TensorContent
```kotlin
@RequiresApi(value = 27)
```class  TensorContent  :  AutoCloseable 
Content read back from a  GlobalTensor . 
#### Parameters
sh Mem 
the Shared memory carrying the content read back from the tensor. 
tensor 
the global tensor being read back from. 
Members 
## Types
Slice 
```kotlin
class Slice(content: TensorContent, range: IntRange)
```
A handy class to easily read a range of the tensor's content. 
## Properties
buffer 
```kotlin
val buffer: ByteBuffer
```
The  ByteBuffer  containing the global tensor's content. 
## Functions
apply Change 
```kotlin
fun applyChange()
```
Write the content back to reset the tensor. This method will use the data current held by this  TensorContent  to override the tensor's content. 
apply Change Suspend 
```kotlin
suspend fun applyChangeSuspend()
```
The suspend version of  applyChange . 
close 
```kotlin
open override fun close()
```
Unmap the buffer and close the shared memory. Do not call any methods after close it. 
get 
```kotlin
operator fun get(index: Int): Number
```
Get a value from the tensor's content by index. The tensor must be of  Tensor.DataType.FLOAT64 ,  Tensor.DataType.FLOAT32 ,  Tensor.DataType.INT32 ,  Tensor.DataType.INT16  or  Tensor.DataType.INT8  datatypes. Otherwise, you may consider to directly use  buffer  to read the content byte-by-byte. 
```kotlin
operator fun get(range: IntRange): TensorContent.Slice
```
Get a range of values from the tensor's content. The tensor must be of  Tensor.DataType.FLOAT64 ,  Tensor.DataType.FLOAT32 ,  Tensor.DataType.INT32 ,  Tensor.DataType.INT16  or  Tensor.DataType.INT8  datatypes. Otherwise, you may consider to directly use  buffer  to read the content byte-by-byte. 
set Data 
```kotlin
fun setData(doubleArray: DoubleArray, offset: Int = 0)
```
If the tensor from which the content is read back is of  Tensor.DataType.FLOAT64  datatype, you can use this method to update the content to an integer array. Then, you can call  applyChange  to apply the update to the tensor. 
```kotlin
fun setData(floatArray: FloatArray, offset: Int = 0)
```
If the tensor from which the content is read back is of  Tensor.DataType.FLOAT32  datatype, you can use this method to update the content to a float array. Then, you can call  applyChange  to apply the update to the tensor. 
```kotlin
fun setData(intArray: IntArray, offset: Int = 0)
```
If the tensor from which the content is read back is of  Tensor.DataType.INT32  datatype, you can use this method to update the content to an integer array. Then, you can call  applyChange  to apply the update to the tensor. 
```kotlin
fun setData(shortArray: ShortArray, offset: Int = 0)
```
If the tensor from which the content is read back is of  Tensor.DataType.INT16  datatype, you can use this method to update the content to an short array. Then, you can call  applyChange  to apply the update to the tensor. 
update 
```kotlin
fun update()
```
Update to the tensor's up-to-date's content. If you have changed the content, but have not call the  applyChange  or  applyChangeSuspend  to write the updated content back to the tensor, the change will be discarded. 
update Suspend 
```kotlin
suspend fun updateSuspend()
```
Suspended version of  update .