# chipColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ChipsDefaults / chipColors 
# chipColors
```kotlin
@Composable
```fun  chipColors ( ) :  ChipColors 
the default chip colors from the theme's color scheme. 
```kotlin
@Composable
```fun  chipColors ( contentColor :  Color  =  Color.Unspecified ,  backgroundColor :  Color  =  Color.Unspecified ) :  ChipColors 
Creates a new  ChipColors  instance with the specified content and background colors. If the colors are not specified, the default colors from the theme's color scheme are used. 
#### Return
A new  ChipColors  instance with the specified or default colors. 
#### Parameters
content Color 
The content color of the chip. Defaults to  Color.Unspecified . 
background Color 
The background color of the chip. Defaults to  Color.Unspecified .