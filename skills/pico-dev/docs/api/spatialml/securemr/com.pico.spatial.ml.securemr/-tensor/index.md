# Tensor | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor 
# Tensor
```kotlin
@RequiresApi(value = 27)
```abstract  class  Tensor ( val  config :  Tensor.InitInfo ) 
Root class of all tensors (global and pipeline). 
#### Parameters
config 
Configuration at initialization. 
#### Inheritors
GlobalTensor PipelineTensor Members 
## Constructors
Tensor 
```kotlin
constructor(config: Tensor.InitInfo)
```
## Types
Color Array Init Info 
```kotlin
class ColorArrayInitInfo(type: Tensor.ColorType, size: Int = 1) : Tensor.SpecialUsageInitInfo
```
Initialization for a RGB or RGBA color array  tensor . 
Color Type 
```kotlin
enum ColorType : Enum<Tensor.ColorType>
```
The color type (combining  DataType  and number of channels) used to define a color array. 
Data Type 
```kotlin
enum DataType : Enum<Tensor.DataType>
```
Data type enums. 
Double Array Init Info 
```kotlin
class DoubleArrayInitInfo(size: Int) : Tensor.SpecialUsageInitInfo
```
Initialization of a  tensor  for double array. If the double values to be contained by the tensor is supposed to be static, you should consider use the  String.tensor  defined in  Pipeline  which allows you to 
Float Array Init Info 
```kotlin
class FloatArrayInitInfo(size: Int) : Tensor.SpecialUsageInitInfo
```
Initialization of a  tensor  for float array. If the float values to be contained by the tensor is supposed to be static, you should consider use the  String.tensor  defined in  Pipeline  which allows you to 
Init Info 
```kotlin
abstract class InitInfo(val dataType: Tensor.DataType, val dimensions: IntArray, usageFlag: Tensor.TensorUsage, channel: Int, specialFlag: Int = 0)
```
The most fundamental initialization configuration for Tensor. 
Int Array Init Info 
```kotlin
class IntArrayInitInfo(size: Int) : Tensor.SpecialUsageInitInfo
```
Initialization of a  tensor  for int array. If the int values to be contained by the tensor is supposed to be static, you should consider use the  String.tensor  defined in  Pipeline  which allows you to 
Multi Dimensional Init Info 
```kotlin
class MultiDimensionalInitInfo(dataType: Tensor.DataType, dimensions: IntArray, channel: Int, dynamicTexture: Boolean = false) : Tensor.InitInfo
```
Initialization config to declare a multi-dimensional tensor. This type of tensors is the conventionally defined ones in mathematics and physics applications. The data given to the tensor will be interpreted as an array of the declared data type. This is the  only  type that support arithmetic operations. 
Point2Array Init Info 
```kotlin
class Point2ArrayInitInfo(dataType: Tensor.DataType, size: Int = 1) : Tensor.SpecialUsageInitInfo
```
Initialization for a POINT2 array  tensor . 
Point3Array Init Info 
```kotlin
class Point3ArrayInitInfo(dataType: Tensor.DataType, size: Int = 1) : Tensor.SpecialUsageInitInfo
```
Initialization for a POINT3 array  tensor . 
Scalar Init Info 
```kotlin
class ScalarInitInfo(dataType: Tensor.DataType, size: Int = 1) : Tensor.SpecialUsageInitInfo
```
Initialization for a SCALAR array  tensor . 
Short Array Init Info 
```kotlin
class ShortArrayInitInfo(size: Int) : Tensor.SpecialUsageInitInfo
```
Initialization of a  tensor  for short array. If the short values to be contained by the tensor is supposed to be static, you should consider use the  String.tensor  defined in  Pipeline  which allows you to 
Slice Init Info 
```kotlin
class SliceInitInfo(dataType: Tensor.DataType, size: Int = 1, channel: Int = 2) : Tensor.SpecialUsageInitInfo
```
Initialization for a SLICE array  tensor . 
Special Usage Init Info 
```kotlin
abstract class SpecialUsageInitInfo(dataType: Tensor.DataType, size: Int, usage: Tensor.TensorUsage, channel: Int) : Tensor.InitInfo
```
Tensor's initialization config for special usage (usages other then the conventional multi-dimensional tensors). 
String Init Info 
```kotlin
class StringInitInfo(size: Int) : Tensor.SpecialUsageInitInfo
```
Initialization of a  tensor  for String. If the string to be contained by the tensor is supposed to be static, you should consider use the  String.tensor  defined in  Pipeline  which allows you to 
Tensor Usage 
```kotlin
enum TensorUsage : Enum<Tensor.TensorUsage>
```
Enum to declare tensor's usage. By default, the tensor shall all be of multi-dimensional usage, which creates non-structured data arrays. Such a tensor observes the conventional definition of tensors in linear algebra, where the values it contains are non-structured. 
Time Stamp Init Info 
```kotlin
class TimeStampInitInfo : Tensor.SpecialUsageInitInfo
```
Initialization for a timestamp 
## Properties
config 
```kotlin
val config: Tensor.InitInfo
```tensor Resource 
```kotlin
open var tensorResource: SharedMemory?
```
The content to the tensor. The provided SharedMemory shall be closed by the caller after the setter completes. 
## Functions
reset Tensor Value 
```kotlin
protected abstract fun resetTensorValue()
```
Callback when the tensor resource is reset