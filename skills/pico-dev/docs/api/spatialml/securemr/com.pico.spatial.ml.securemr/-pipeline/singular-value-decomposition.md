# singularValueDecomposition | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / singularValueDecomposition 
# singularValueDecomposition
```kotlin
fun singularValueDecomposition(source: Tensor, wResult: Tensor?, uResult: Tensor?, vtResult: Tensor?)
```
Perform singular value decomposition of a matrix. 
#### Parameters
source 
the matrix to be decomposed. It must be a multi-dimensional tensor of 2 dimensions:  M x N . The data type must be  DataType.FLOAT64 ,  DataType.FLOAT32 ,  DataType.Image.R_FLOAT ,  DataType.Image.R_DOUBLE  or  DataType.Image.R_FLOAT_DYNAMIC . 
w Result 
an optional result for the W part of the SVD. It must be a multi-dimensional tensor of 2 dimensions. The data type must be  DataType.FLOAT64 ,  DataType.FLOAT32 ,  DataType.Image.R_FLOAT ,  DataType.Image.R_DOUBLE  or  DataType.Image.R_FLOAT_DYNAMIC . The 2 dimensions must be  min(M, N)  and  1 . 
u Result 
an optional result for the U part of the SVD. It must be a multi-dimensional tensor of 2 dimensions. The data type must be  DataType.FLOAT64 ,  DataType.FLOAT32 ,  DataType.Image.R_FLOAT ,  DataType.Image.R_DOUBLE  or  DataType.Image.R_FLOAT_DYNAMIC . The two dimensions must be  M  and  min(M, N) . 
vt Result 
an optional result for the VT part of the SVD. It must be a multi-dimensional tensor of 2 dimensions. The data type must be  DataType.FLOAT64 ,  DataType.FLOAT32 ,  DataType.Image.R_FLOAT ,  DataType.Image.R_DOUBLE  or  DataType.Image.R_FLOAT_DYNAMIC . The two dimensions must be  min(M, N)  and  N . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.