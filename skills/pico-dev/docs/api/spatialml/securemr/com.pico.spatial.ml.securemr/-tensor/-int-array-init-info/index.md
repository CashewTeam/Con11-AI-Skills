# IntArrayInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / IntArrayInitInfo 
# IntArrayInitInfo
```kotlin
class IntArrayInitInfo(size: Int) : Tensor.SpecialUsageInitInfo
```
Initialization of a  tensor  for int array. If the int values to be contained by the tensor is supposed to be static, you should consider use the  String.tensor  defined in  Pipeline  which allows you to 

```
with(pipeline) { val arrTensor = intArrayOf(1, 2, 3, 4, 5).tensor // or for single int: val iVal = 10 val scalarTensor = iVal.tensor}
```
with in a  Pipeline  scope. 
Note  here, since a INT ARRAY tensor is a special-usage tensor, it is not the exact tensor as we have been using in mathematics and physics. Rather, the word  tensor  represents an opaque handle or an abstraction of data, that your application hands over to SecureMR service to process. 
A INT ARRAY is equivalent to as a single-dimension array of INT32 values. 
#### Parameters
size 
: number of int values to be contained by this tensor. 
Members 
## Constructors
Int Array Init Info 
```kotlin
constructor(size: Int)
```