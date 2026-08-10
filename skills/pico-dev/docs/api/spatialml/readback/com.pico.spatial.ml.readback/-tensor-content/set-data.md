# setData | PICO Spatial SDK

spatialml:readback / com.pico.spatial.ml.readback / TensorContent / setData 
# setData
```kotlin
fun setData(shortArray: ShortArray, offset: Int = 0)
```
If the tensor from which the content is read back is of  Tensor.DataType.INT16  datatype, you can use this method to update the content to an short array. Then, you can call  applyChange  to apply the update to the tensor. 
#### Parameters
short Array 
the short array to update the content. 
offset 
from where the data setting starts.  offset  * 2 bytes will be skipped in  buffer . 
#### Throws
Spatial MLException 
if the tensor from which the content is read back is not of  Tensor.DataType.INT16  datatype. 
```kotlin
fun setData(intArray: IntArray, offset: Int = 0)
```
If the tensor from which the content is read back is of  Tensor.DataType.INT32  datatype, you can use this method to update the content to an integer array. Then, you can call  applyChange  to apply the update to the tensor. 
#### Parameters
int Array 
the integer array to update the content. 
offset 
from where the data setting starts.  offset  * 4 bytes will be skipped in  buffer . 
#### Throws
Spatial MLException 
if the tensor from which the content is read back is not of  Tensor.DataType.INT32  datatype. 
```kotlin
fun setData(floatArray: FloatArray, offset: Int = 0)
```
If the tensor from which the content is read back is of  Tensor.DataType.FLOAT32  datatype, you can use this method to update the content to a float array. Then, you can call  applyChange  to apply the update to the tensor. 
#### Parameters
float Array 
the integer array to update the content. 
offset 
from where the data setting starts.  offset  * 4 bytes will be skipped in  buffer . 
#### Throws
Spatial MLException 
if the tensor from which the content is read back is not of  Tensor.DataType.FLOAT32  datatype. 
```kotlin
fun setData(doubleArray: DoubleArray, offset: Int = 0)
```
If the tensor from which the content is read back is of  Tensor.DataType.FLOAT64  datatype, you can use this method to update the content to an integer array. Then, you can call  applyChange  to apply the update to the tensor. 
#### Parameters
double Array 
the double array to update the content. 
offset 
from where the data setting starts.  offset  * 8 bytes will be skipped in  buffer . 
#### Throws
Spatial MLException 
if the tensor from which the content is read back is not of  Tensor.DataType.FLOAT64  datatype.