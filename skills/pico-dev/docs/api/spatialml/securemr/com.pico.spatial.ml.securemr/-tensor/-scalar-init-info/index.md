# ScalarInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / ScalarInitInfo 
# ScalarInitInfo
```kotlin
class ScalarInitInfo(dataType: Tensor.DataType, size: Int = 1) : Tensor.SpecialUsageInitInfo
```
Initialization for a SCALAR array  tensor . 
It is not recommended to create a  Tensor  from  ScalarInitInfo  directly. It is recommended to use  StringInitInfo ,  ShortArrayInitInfo ,  IntArrayInitInfo ,  FloatArrayInitInfo , and  DoubleArrayInitInfo  instead. 
Note  here, since a SCALAR array tensor is a special-usage tensor, it is not the exact tensor as we have been using in mathematics and physics. Rather, the word  tensor  represents an opaque handle or an abstraction of data, that your application hands over to SecureMR service to process. 
A SCALAR array is a single-dimension array of 1-channel elements. It is the same as a multi-dimensional tensor with dimensions = N, 1 or 1, N. Yet, a scalar array is used when there is no need to distinguish row-v.s.-column vector, such as an array of texture or material indices. Also, the introduction of SCALAR array allows for a syntax sugar, where you can directly use an  Array<T>  object in Kotlin, as a SecureMR tensor when you call any  Pipeline  methods. The SecureMR tensor automatically boxed from  Array<T>  will be of SCALAR array usage. 
#### Parameters
data Type 
: data type of values in this scalar array. 
size 
: number of the elements. 
#### See also
Pipeline Members 
## Constructors
Scalar Init Info 
```kotlin
constructor(dataType: Tensor.DataType, size: Int = 1)
```