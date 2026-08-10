# ColorArrayInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / ColorArrayInitInfo 
# ColorArrayInitInfo
```kotlin
class ColorArrayInitInfo(type: Tensor.ColorType, size: Int = 1) : Tensor.SpecialUsageInitInfo
```
Initialization for a RGB or RGBA color array  tensor . 
Note  here, since a color array tensor is a special-usage tensor, it is not the exact tensor as we have been using in mathematics and physics. Rather, the word  tensor  represents an opaque handle or an abstraction of data, that your application hands over to SecureMR service to process. 
A RGB or RGBA color array is a single-dimension array of RGBA elements, where each element has four components (or to say, values): R, G, B and A (optional). They must be of the same data type. Auto-boxing from Kotlin  android.graphics.Color  is also supported. 
#### Parameters
type 
: color type of the color values in the array. 
size 
: number of the elements. 
Members 
## Constructors
Color Array Init Info 
```kotlin
constructor(type: Tensor.ColorType, size: Int = 1)
```