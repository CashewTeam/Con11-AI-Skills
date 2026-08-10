# calculatePosition | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows.popup / HorizontalPlacement / calculatePosition 
# calculatePosition
```kotlin
abstract fun calculatePosition(density: Density, anchorBounds: IntRect, windowSize: IntSize, layoutDirection: LayoutDirection, popupContentSize: IntSize): Int
```
Calculates the horizontal position of a  Popup  on screen. 
The window size is useful in cases where the popup is meant to be positioned next to its anchor instead of inside of it. The size can be used to calculate available space around the parent to find a spot with enough clearance (e.g. when implementing a dropdown). Note that positioning the popup outside of the window bounds might prevent it from being visible. 
#### Return
The window relative position where the popup should be positioned. 
#### Parameters
density 
The density use to calculate the position. 
anchor Bounds 
The window relative bounds of the layout which this popup is anchored to. 
window Size 
The size of the window containing the anchor layout. 
layout Direction 
The layout direction of the anchor layout. 
popup Content Size 
The size of the popup's content.