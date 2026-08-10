# copy | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ToggleableChipColors / copy 
# copy
```kotlin
fun copy(contentColor: Color = this.contentColor, backgroundColor: Color = this.backgroundColor, activeContentColor: Color = this.activeContentColor, activeBackgroundColor: Color = this.activeBackgroundColor): ToggleableChipColors
```
Create a new  ToggleableChipColors  instance with the specified color properties. If some color values are not provided, the color values of the current instance are used. 
#### Return
A new  ToggleableChipColors  instance with the specified properties. 
#### Parameters
content Color 
The content color of the chip. If not provided, the content color of the current instance is used. 
background Color 
The background color of the chip. If not provided, the background color of the current instance is used. 
active Content Color 
The content color when the toggle state is on. If not provided, the active content color of the current instance is used. 
active Background Color 
The background color when the toggle state is on. If not provided, the active background color of the current instance is used.