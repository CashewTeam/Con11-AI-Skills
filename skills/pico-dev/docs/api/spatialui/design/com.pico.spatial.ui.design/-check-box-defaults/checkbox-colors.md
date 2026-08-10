# checkboxColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / CheckBoxDefaults / checkboxColors 
# checkboxColors
```kotlin
@Composable
```fun  checkboxColors ( ) :  CheckboxColor 
the default colors from the theme's color scheme of checkbox . 
```kotlin
@Composable
```fun  checkboxColors ( backgroundColor :  Color  =  Color.Unspecified ,  contentColor :  Color  =  Color.Unspecified ,  borderColor :  Color  =  Color.Unspecified ) :  CheckboxColor 
Creates a  CheckboxColor  that represents the default container and content colors used in a  Checkbox . 
#### Return
The new  CheckboxColor  with expected background color, content color and border color. 
#### Parameters
background Color 
the container color of this  Checkbox  when enabled. 
content Color 
the content color of this  Checkbox  when enabled. 
border Color 
the border color of this  Checkbox  when enabled.