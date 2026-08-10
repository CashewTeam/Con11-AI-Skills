# HorizontalPlacement | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows.popup / HorizontalPlacement 
# HorizontalPlacement
```kotlin
interface HorizontalPlacement
```
A  HorizontalPlacement  is used to position a  Popup  horizontally relative to its anchor. 
Members 
## Types
Companion 
```kotlin
object Companion
```
Companion 
## Functions
calculate Position 
```kotlin
abstract fun calculatePosition(density: Density, anchorBounds: IntRect, windowSize: IntSize, layoutDirection: LayoutDirection, popupContentSize: IntSize): Int
```
Calculates the horizontal position of a  Popup  on screen.