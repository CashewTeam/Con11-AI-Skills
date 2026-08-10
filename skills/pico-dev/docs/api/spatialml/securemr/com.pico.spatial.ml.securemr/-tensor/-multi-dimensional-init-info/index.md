# MultiDimensionalInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / MultiDimensionalInitInfo 
# MultiDimensionalInitInfo
```kotlin
class MultiDimensionalInitInfo(dataType: Tensor.DataType, dimensions: IntArray, channel: Int, dynamicTexture: Boolean = false) : Tensor.InitInfo
```
Initialization config to declare a multi-dimensional tensor. This type of tensors is the conventionally defined ones in mathematics and physics applications. The data given to the tensor will be interpreted as an array of the declared data type. This is the  only  type that support arithmetic operations. 
#### Parameters
data Type 
the data type of each values in the tensor. 
dimensions 
the sizes along each dimensions of the tensor.  Note  here we require there must be at least 2 dimensions. If you desire a vector, you will still need 2 dimensions to distinguish a row vector or a column vector. Hence, you will need to specify the dimensions as 1, N or N, 1. 
channel 
Note: it is not recommended to set this parameter explicitly. If you want to declare a tensor of multi-channel pixel type, use  DataType.Image  instead . The specifies the number of values consisting each element in this tensor. The usage of channel is the same as that in OpenCV. For example, you may need a tensor to store a 1024x2048 RGB image. You can declare the tensor's dimensions to be 1024, 2048, 3 with channel = 1, or 1024, 2048 with channel = 3. However, the former one will gives you 1024 matrices of shape 2048x3, which will make it not suitable for your CV post-processing operations. Yet, the latter one generate a tensor of single 1024x2048 matrices, with 1024x2048  elements , each of which consists of 3  values . Hence, CV operations like affine or matrix multiplication can still work on this tensor. 
dynamic Texture 
whether the tensor will be used as a dynamic texture. A dynamic-texture tensor can be used as the texture fields for scene graph materials. 
#### See also
Scene Graph Property. PBRMaterials. Base Color Texture Scene Graph Property. PBRMaterials. Metallic Texture Scene Graph Property. PBRMaterials. Roughness Texture Tensor. DataType. Image Members 
## Constructors
Multi Dimensional Init Info 
```kotlin
constructor(dataType: Tensor.DataType, dimensions: IntArray, channel: Int, dynamicTexture: Boolean = false)
```
```kotlin
constructor(dataType: Tensor.DataType, dimensions: IntArray)
```
Initialization config to declare a multi-dimensional tensor. This type of tensors is the conventionally defined ones in mathematics and physics applications. The data given to the tensor will be interpreted as an array of the declared data type and channels. This is the  only  type that support arithmetic operations. 
```kotlin
constructor(dataType: Tensor.DataType.Image, dimensions: IntArray)
```
Initialization config to declare a multi-dimensional tensor for textures or images, where each element in the tensor is a multi-channel pixel. This type of tensors is the conventionally defined ones in mathematics and physics applications. The data given to the tensor will be interpreted as an array of the declared data type. This is the  only  type that support arithmetic operations.