# SpecialUsageInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / SpecialUsageInitInfo 
# SpecialUsageInitInfo
```kotlin
abstract class SpecialUsageInitInfo(dataType: Tensor.DataType, size: Int, usage: Tensor.TensorUsage, channel: Int) : Tensor.InitInfo
```
Tensor's initialization config for special usage (usages other then the conventional multi-dimensional tensors). 
#### Parameters
data Type 
data type. 
size 
the number of elements. 
usage 
the special usage type. 
channel 
the number of values per element. 
#### Inheritors
Point2ArrayInitInfo Point3ArrayInitInfo ScalarInitInfo StringInitInfo ShortArrayInitInfo IntArrayInitInfo FloatArrayInitInfo DoubleArrayInitInfo SliceInitInfo ColorArrayInitInfo TimeStampInitInfo Members 
## Constructors
Special Usage Init Info 
```kotlin
constructor(dataType: Tensor.DataType, size: Int, usage: Tensor.TensorUsage, channel: Int)
```