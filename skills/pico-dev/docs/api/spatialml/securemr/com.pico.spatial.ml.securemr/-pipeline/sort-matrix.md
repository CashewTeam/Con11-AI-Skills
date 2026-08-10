# sortMatrix | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / sortMatrix 
# sortMatrix
```kotlin
fun sortMatrix(sortType: Pipeline.SortType, source: Tensor, sortedResult: Tensor?, indexResult: Tensor?)
```
Sort a matrix, column-by-column or row-by-row. 
#### Parameters
sort Type 
whether the sort should be done column-wisely or row-wisely. 
source 
the matrix to be sorted. It must be a multi-dimensional tensor of 2 dimensions. Its data type must either be non-pixel datatype, or RED-channel-only pixel types. Multi-channel pixel types such as  RG_FLOAT , or  R8G8B8A8_U  are not allowed. 
sorted Result 
the optional result to store the sorted matrix. The tensor must have the the same init info as the  source , i.e., the same dimensions and the same datatype. 
index Result 
the optional result to store the original indices of matrix elements in  source 's row/column, according to the  sortType . It must be a multi-dimensional tensor with the same dimensions as the  source , but its datatype must be integral and must not be a multi-channel pixel type, e.g.,  DataType.INT16  is accepted, but  DataType.Image.R16G16_S  is not. 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.