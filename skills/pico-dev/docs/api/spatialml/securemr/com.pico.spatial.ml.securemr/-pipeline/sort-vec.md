# sortVec | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / sortVec 
# sortVec
```kotlin
fun sortVec(source: Tensor, sortedResult: Tensor?, indexResult: Tensor?)
```
Sort a scalar array. 
#### Parameters
source 
the tensor to be sorted, must be a 1D scalar array tensor of size  N , i.e., it must be initialized using  Tensor.ScalarInitInfo ,  Tensor.StringInitInfo ,  Tensor.ShortArrayInitInfo ,  Tensor.IntArrayInitInfo ,  Tensor.FloatArrayInitInfo  or  Tensor.DoubleArrayInitInfo . 
sorted Result 
the optional result, to store the sorted tensor. Its init info must be the same as that of the  source , i.e, the init info class, the datatype and the size must all be the same. 
index Result 
the optional result, to store the original indices of elements in  source  after being sorted. It must be a integral scalar array, of size  N , i.e., must be initialized using  Tensor.StringInitInfo ,  Tensor.ShortArrayInitInfo ,  Tensor.IntArrayInitInfo , or  Tensor.ScalarInitInfo  with  datatype  being one of  DataType.UINT8 ,  DataType.INT8 ,  DataType.UINT16 ,  DataType.INT16  or  DataType.INT32 . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.