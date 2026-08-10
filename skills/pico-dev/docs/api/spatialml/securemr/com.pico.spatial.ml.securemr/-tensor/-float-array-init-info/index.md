# FloatArrayInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / FloatArrayInitInfo 
# FloatArrayInitInfo
```kotlin
class FloatArrayInitInfo(size: Int) : Tensor.SpecialUsageInitInfo
```
Initialization of a  tensor  for float array. If the float values to be contained by the tensor is supposed to be static, you should consider use the  String.tensor  defined in  Pipeline  which allows you to 

```
with(pipeline) { val arrTensor = floatArrayOf(0.001f, -0.002f, 0.003f, 5.555e10f).tensor // or for single float: val fVal = 10.0f val scalarTensor = fVal.tensor}
```
with in a  Pipeline  scope. 
Note  here, since a FLOAT ARRAY tensor is a special-usage tensor, it is not the exact tensor as we have been using in mathematics and physics. Rather, the word  tensor  represents an opaque handle or an abstraction of data, that your application hands over to SecureMR service to process. 
A FLOAT ARRAY is equivalent to as a single-dimension array of FLOAT32 values. 
#### Parameters
size 
: number of int values to be contained by this tensor. 
Members 
## Constructors
Float Array Init Info 
```kotlin
constructor(size: Int)
```