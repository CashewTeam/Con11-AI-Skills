# argmax | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / argmax 
# argmax
```kotlin
fun argmax(source: Tensor, result: Tensor)
```
Compute argmax operation on tensor, giving the indices of max element of the input tensor. 
For example, the  source  may be 2x3 tensor:  [[1, 2, 3], [6, 5, 4]] , where the argmax is the index of "6":  (1, 0) . Hence, the  result  should be of a tensor with dimensions: 1x2, in order to store this  (1, 0)  value. 
If the  source  is a RGB tensor instead, for example: 
- 
RED channel:  `` [[1, 2, 3], [6, 5, 4]] `` 
- 
GREEN channel:  `` [[4, 5, 6], [1, 2, 3]] `` 
- 
BLUE channel:  `` [[1, 3, 5], [4, 6, 2]] ``  As the argmax is performed per-channel, the   argmax result on the 1st channel is  (1, 0) ,  (0, 2)  on the 2nd and  (1, 1)  on the 3rd.   In this case, the  result  is expected to store all three dual-value indices, so it should   be a tensor with dimensions such as 3x2, whose content will be 

```
[     [1,0],     [0,2],     [1,1],]
```
#### Parameters
source 
The input to argmax. It must be a multi-dimensional tensor. If it is an image tensor with multi-channel pixel datatype, the max will be computed per channel. 
result 
The required result, to store the indices of the max elements in  source . The  result  must be a multi-dimensional tensor of integral datatype. Its dimensions must be  C x D , where:     *  C  is 1 if the  source  tensor's datatype is a non-pixel one,     * otherwise,  C  is the number of channels in each of  source  tensor's pixel. For       example, if  source  tensor is an image with DataType.Image.RGB_FLOAT pixels,  C        is 3.     *  D  is the number of dimensions in  source . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.