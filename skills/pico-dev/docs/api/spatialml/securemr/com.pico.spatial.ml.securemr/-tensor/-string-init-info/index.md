# StringInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / StringInitInfo 
# StringInitInfo
```kotlin
class StringInitInfo(size: Int) : Tensor.SpecialUsageInitInfo
```
Initialization of a  tensor  for String. If the string to be contained by the tensor is supposed to be static, you should consider use the  String.tensor  defined in  Pipeline  which allows you to 

```
with(pipeline) { val stringTensor = "This is a test String".tensor}
```
with in a  Pipeline  scope. 
Note  here, since a STRING tensor is a special-usage tensor, it is not the exact tensor as we have been using in mathematics and physics. Rather, the word  tensor  represents an opaque handle or an abstraction of data, that your application hands over to SecureMR service to process. 
A STRING tensor is equivalent to as a single-dimension array of UINT8 values, containing the bytes of the string encoded in UTF-8. 
#### Parameters
size 
: number of the bytes of the string in UTF-8. 
Members 
## Constructors
String Init Info 
```kotlin
constructor(size: Int)
```