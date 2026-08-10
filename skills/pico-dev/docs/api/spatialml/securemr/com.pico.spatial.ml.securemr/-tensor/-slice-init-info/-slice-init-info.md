# SliceInitInfo | PICO Spatial SDK

spatialml:securemr / com.pico.spatial.ml.securemr / Tensor / SliceInitInfo / SliceInitInfo 
# SliceInitInfo
```kotlin
constructor(dataType: Tensor.DataType, size: Int = 1, channel: Int = 2)
```
#### Parameters
data Type 
: data type of slice start, end and skip (must be the same). Only integral types are allowed. 
size 
: number of the elements. 
channel 
number of channels, either 2 or 3; 2 means the slice is expressed as  [START, END]  whereas 3 means  [START, END, SKIP] .