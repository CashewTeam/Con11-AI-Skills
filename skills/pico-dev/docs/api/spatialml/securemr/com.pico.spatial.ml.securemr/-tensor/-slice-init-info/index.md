# SliceInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / SliceInitInfo 
# SliceInitInfo
```kotlin
class SliceInitInfo(dataType: Tensor.DataType, size: Int = 1, channel: Int = 2) : Tensor.SpecialUsageInitInfo
```
Initialization for a SLICE array  tensor . 
Note  here, since a SLICE array tensor is a special-usage tensor, it is not the exact tensor as we have been using in mathematics and physics. Rather, the word  tensor  represents an opaque handle or an abstraction of data, that your application hands over to SecureMR service to process. 
A SLICE array contains one or multiple slice element. A slice element is a python-like slice over one dimension, such as {0, 5} means taking the first 5 ones, {0, -1} means taking all, {0, 10, 2} means taking the ones only with even index. Hence, a SLICE array must either be of 2 or 3 channels, where values in each elements means {slice start, slice end} or {slice start, slice end, slice skip}. 
For example, if you want to take the middle 256x256 elements from the first matrix in a 3x1024x2048 tensor, here will be the SLICE array you may use: {{1, 2}, {384, 640}, {896, 1152}}. If you want to flip along the last dimension additionally: {{1, 2, 1}, {384, 640, 1}, {1151, 895, -1}} 
With the help of SLICE array tensor, we enable a syntax sugar for  PipelineTensor . When you want to use only a portion of  PipelineTensor tensor1 , you can directly use  tensor1[0..5, 0..1]  or  tensor1[tensor2]  where  tensor2  is a pre-defined SLICE array tensor. 
#### Parameters
data Type 
: data type of slice start, end and skip (must be the same). Only integral types are allowed. 
size 
: number of the elements. 
channel 
number of channels, either 2 or 3; 2 means the slice is expressed as  [START, END]  whereas 3 means  [START, END, SKIP] . 
#### See also
Pipeline Tensor Members 
## Constructors
Slice Init Info 
```kotlin
constructor(dataType: Tensor.DataType, size: Int = 1, channel: Int = 2)
```