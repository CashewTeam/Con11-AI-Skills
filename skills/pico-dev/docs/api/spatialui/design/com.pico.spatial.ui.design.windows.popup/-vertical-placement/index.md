# VerticalPlacement | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows.popup / VerticalPlacement 
# VerticalPlacement
```kotlin
interface VerticalPlacement
```
A  VerticalPlacement  is used to position a  Popup  vertically relative to its anchor. 
Members 
## Types
Companion 
```kotlin
object Companion
```
companion 
## Functions
calculate Position 
```kotlin
abstract fun calculatePosition(density: Density, anchorBounds: IntRect, windowSize: IntSize, popupContentSize: IntSize): Int
```
Calculates the position of a  Popup  on screen.