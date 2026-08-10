# DoubleArrayInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / DoubleArrayInitInfo 
# DoubleArrayInitInfo
```kotlin
class DoubleArrayInitInfo(size: Int) : Tensor.SpecialUsageInitInfo
```
Initialization of a  tensor  for double array. If the double values to be contained by the tensor is supposed to be static, you should consider use the  String.tensor  defined in  Pipeline  which allows you to 

```
with(pipeline) { val arrTensor = doubleArrayOf(0.001, -0.002, 0.003, 5.555e10).tensor // or for single double: val dVal = 10.0 val scalarTensor = dVal.tensor}
```
with in a  Pipeline  scope. 
Note  here, since a DOUBLE ARRAY tensor is a special-usage tensor, it is not the exact tensor as we have been using in mathematics and physics. Rather, the word  tensor  represents an opaque handle or an abstraction of data, that your application hands over to SecureMR service to process. 
A DOUBLE ARRAY is equivalent to as a single-dimension array of FLOAT64 values. 
#### Parameters
size 
: number of double values to be contained by this tensor. 
Members 
## Constructors
Double Array Init Info 
```kotlin
constructor(size: Int)
```