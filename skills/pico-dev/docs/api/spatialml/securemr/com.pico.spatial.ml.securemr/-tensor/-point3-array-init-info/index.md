# Point3ArrayInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / Point3ArrayInitInfo 
# Point3ArrayInitInfo
```kotlin
class Point3ArrayInitInfo(dataType: Tensor.DataType, size: Int = 1) : Tensor.SpecialUsageInitInfo
```
Initialization for a POINT3 array  tensor . 
Note  here, since a POINT3 array tensor is a special-usage tensor, it is not the exact tensor as we have been using in mathematics and physics. Rather, the word  tensor  represents an opaque handle or an abstraction of data, that your application hands over to SecureMR service to process. 
A POINT3 array is a single-dimension array of POINT3 elements, where each element has three components (or to say, values): X, Y and Z coordinates. They must be of the same data type. Hence, such an array is designed for representing 3D points. 
#### Parameters
data Type 
: data type of the X, Y and Z values in this POINT3 array. 
size 
: number of the elements. 
Members 
## Constructors
Point3Array Init Info 
```kotlin
constructor(dataType: Tensor.DataType, size: Int = 1)
```