# toggleableChipColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ChipsDefaults / toggleableChipColors 
# toggleableChipColors
```kotlin
@Composable
```fun  toggleableChipColors ( ) :  ToggleableChipColors 
the default toggleable chip colors from the theme's color scheme. 
```kotlin
@Composable
```fun  toggleableChipColors ( contentColor :  Color  =  Color.Unspecified ,  backgroundColor :  Color  =  Color.Unspecified ,  activeContentColor :  Color  =  Color.Unspecified ,  activeBackgroundColor :  Color  =  Color.Unspecified ) :  ToggleableChipColors 
Creates a new  ToggleableChipColors  instance with the specified content and background colors. If the colors are not specified, the default colors from the theme's color scheme are used. 
#### Return
A new  ToggleableChipColors  instance with the specified or default colors. 
#### Parameters
content Color 
The content color of the chip. Defaults to  Color.Unspecified . 
background Color 
The background color of the chip. Defaults to  Color.Unspecified . 
active Content Color 
The content color when the toggle state is on. Defaults to  Color.Unspecified . 
active Background Color 
The background color when the toggle state is on. Defaults to  Color.Unspecified .