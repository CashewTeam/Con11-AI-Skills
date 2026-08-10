# ShortArrayInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / ShortArrayInitInfo 
# ShortArrayInitInfo
```kotlin
class ShortArrayInitInfo(size: Int) : Tensor.SpecialUsageInitInfo
```
Initialization of a  tensor  for short array. If the short values to be contained by the tensor is supposed to be static, you should consider use the  String.tensor  defined in  Pipeline  which allows you to 

```
with(pipeline) { val shortTensor = shortArrayOf(1, 2, 3, 4, 5).tensor // or for single short: val shortVal: Short = 10 val shortScalarTensor = shortVal.tensor}
```
with in a  Pipeline  scope. 
Note  here, since a SHORT ARRAY tensor is a special-usage tensor, it is not the exact tensor as we have been using in mathematics and physics. Rather, the word  tensor  represents an opaque handle or an abstraction of data, that your application hands over to SecureMR service to process. 
A SHORT ARRAY is equivalent to as a single-dimension array of INT16 values. 
#### Parameters
size 
: number of shorts to be contained by this tensor. 
Members 
## Constructors
Short Array Init Info 
```kotlin
constructor(size: Int)
```