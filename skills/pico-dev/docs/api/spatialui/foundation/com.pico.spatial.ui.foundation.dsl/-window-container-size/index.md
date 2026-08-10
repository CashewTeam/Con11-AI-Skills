# WindowContainerSize | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / WindowContainerSize 
# WindowContainerSize
```kotlin
class WindowContainerSize
```
The size of the  WindowContainer . support both  Dp  and  LengthUnit . 
provider two constructors: 
- 
WindowContainerSize  with  Dp  as the unit 
- 
WindowContainerSize  with  LengthUnit  as the unit, and  Float  as the value 
Members 
## Constructors
Window Container Size 
```kotlin
constructor(width: Float, height: Float, depth: Float, unit: LengthUnit?)
```
```kotlin
constructor(width: Dp, height: Dp, depth: Dp = Dp.Unspecified)
```