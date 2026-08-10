# depthOffset | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / DepthAlignment / depthOffset 
# depthOffset
```kotlin
abstract fun depthOffset(depth: Int, space: Int): Int
```
Calculates the depth offset based on the bias factor. 
#### Return
Rounded integer offset value. 
#### Parameters
depth 
The depth size of the element. 
space 
The available depth space in the parent container.