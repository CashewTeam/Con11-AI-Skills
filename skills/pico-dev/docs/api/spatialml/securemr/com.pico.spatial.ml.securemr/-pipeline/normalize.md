# normalize | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / normalize 
# normalize
```kotlin
fun normalize(type: Pipeline.NormalizeType, source: Tensor, alphaBeta: Tensor?, result: Tensor)
```
Normalize a tensor. 
#### Parameters
type 
normalization type. 
source 
input tensor, to be normalized. It must be a multi-dimensional tensor. 
alpha Beta 
an optional tensor, to specify the alpha and beta values for the normalization. The tensor must have two values, whatever the usage it is. The first value will be read as alpha, and the second as beta. If not provided, the default alpha and beta will be 1.0 and 0.0 respectively. The data type must be 32-/64-bit float. It can be 1x2, 2x1, 2x1x1, 1x2x1, ... , multi-dimensional tensor of datatype  DataType.FLOAT32  or  DataType.FLOAT64 , or a Point2 array of size 1, where the X value will be read as the alpha and the Y as the beta. Alternatively, although it is not recommended, yet it is valid to use a 1x1 image tensor with pixel datatype being  DataType.Image.RG_FLOAT  or  DataType.Image.RG_DOUBLE , where the RED value is the alpha, and GREEN value being the beta. 
result 
the required tensor, to store the normalized result of the input  source . It must be a multi-dimensional tensor, with the same data type and dimensions as  source , i.e., they must be created with the same  Tensor.InitInfo .