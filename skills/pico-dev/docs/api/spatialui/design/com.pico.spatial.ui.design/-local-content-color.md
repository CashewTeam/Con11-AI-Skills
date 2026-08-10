# LocalContentColor | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / LocalContentColor 
# LocalContentColor
```kotlin
val LocalContentColor: ProvidableCompositionLocal<Color>
```
CompositionLocal containing the preferred content color for a given position in the hierarchy. 
This color should be used for any typography / iconography, to ensure that the color of these adjusts when the background color changes. For example, on a dark background, text should be light, and on a light background, text should be dark. 
Defaults to  Color.Unspecified  if no color has been explicitly set.