# InitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / InitInfo 
# InitInfo
```kotlin
abstract class InitInfo(val dataType: Tensor.DataType, val dimensions: IntArray, usageFlag: Tensor.TensorUsage, channel: Int, specialFlag: Int = 0)
```
The most fundamental initialization configuration for Tensor. 
#### Parameters
data Type 
basic data type of the tensor's content. 
dimensions 
an array of sizes along each dimension of the tensor, describing the tensor's shape. 
usage Flag 
usage flag of the tensor, declaring whether the tensor will be used as a multi-dimensional tensor, or storing structured data for specific usage. 
channel 
number of tensor, i.e., how many values of basic data types each element in this tensor consists of. e.g., a 2D RGB image of UINT8 data type will have three channels, because each element (pixel) in this image contains 3 UINT8 values, and such a 3-channel UINT8 tensor will therefore represent a R8G8B8 image. 
special Flag 
special flag for the tensor's declaration. 
#### Inheritors
MultiDimensionalInitInfo SpecialUsageInitInfo Members 
## Constructors
Init Info 
```kotlin
constructor(dataType: Tensor.DataType, dimensions: IntArray, usageFlag: Tensor.TensorUsage, channel: Int, specialFlag: Int = 0)
```
## Properties
data Type 
```kotlin
val dataType: Tensor.DataType
```dimensions 
```kotlin
val dimensions: IntArray
```is Dynamic Texture 
```kotlin
val isDynamicTexture: Boolean
```
Whether this tensor is a dynamic-texture tensor. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```