# DepthAlignment | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.layout / DepthAlignment 
# DepthAlignment
```kotlin
@Stable
```interface  DepthAlignment 
Depth alignment defines how an element is aligned along the depth axis (usually the Z-axis) of a three-dimensional coordinate system, and determines the offset applied to the element in that axis. 
Members 
## Types
Companion 
```kotlin
object Companion
```
Predefined depth alignment instances. 
## Functions
depth Offset 
```kotlin
abstract fun depthOffset(depth: Int, space: Int): Int
```
Calculates the depth offset based on the bias factor.