# switchCHWAndHWC | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Pipeline / switchCHWAndHWC 
# switchCHWAndHWC
```kotlin
fun switchCHWAndHWC(source: Tensor, result: Tensor)
```
Switch tensor content between a CHW and HWC format. A tensor of CHW format means it is a multi-dimensional tensor of datatype =  Tensor.DataType , and 3 dimensions:  C x H x W . A tensor of HWC format means it is a multi-dimensional tensor of 2 dimensions:  H x W , with datatype =  Tensor.DataType.Image . 
For example, when you get an RGB image content in a multi-dimensional tensor, e.g. a tensor created using: 

```
auto tensor1 = pipeline.newLocalTensor(MultiDimensionalInitInfo(                       DataType.Image.R8G8B8_U,                       intArrayOf(1024, 960))
```
But your algorithm, for instance, trained using PyTorch, requires input as a 3 matrices stack together, i.e., a tensor created using 

```
auto tensor2 = pipeline.newLocalTensor(MultiDimensionalInitInfo(                       DataType.UINT8, intArrayOf(3, 1024, 960))
```
Under such circumstance, this method allow you to efficiently extract the R, G, and B channel from the  tensor1  and assign per-channel image to subtensor  tensor2[0] ,  tensor2[1]  and  tensor2[2] : 
```
pipeline.switchCHWAndHWC(tensor1, tensor2)
```
#### Parameters
source 
the tensor whose format to be switched. It must either be of CHW format, or HWC format. 
result 
the required result to store the switch result. If  source  is of CHW format, it must be of HWC format. If  source  is of HWC format, it must be of CHW format. The data type must be the same as that of  source . 
#### Throws
Spatial MLException 
If the usage is not allowed by the SpatialML run-time Framework, or if the framework encounters internal error and cannot perform the requested behavior.