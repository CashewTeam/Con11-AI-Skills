# Point2ArrayInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / Point2ArrayInitInfo 
# Point2ArrayInitInfo
```kotlin
class Point2ArrayInitInfo(dataType: Tensor.DataType, size: Int = 1) : Tensor.SpecialUsageInitInfo
```
Initialization for a POINT2 array  tensor . 
Note  here, since a POINT2 array tensor is a special-usage tensor, it is not the exact tensor as we have been using in mathematics and physics. Rather, the word  tensor  represents an opaque handle or an abstraction of data, that your application hands over to SecureMR service to process. 
A POINT2 array is a single-dimension array of POINT2 elements, where each element has two components (or to say, values): X coordinate and Y coordinate. They must be of the same data type. Hence, such an array is designed for representing 2D points. 
#### Parameters
data Type 
: data type of the X and Y values in this POINT2 array. 
size 
: number of the elements. 
Members 
## Constructors
Point2Array Init Info 
```kotlin
constructor(dataType: Tensor.DataType, size: Int = 1)
```