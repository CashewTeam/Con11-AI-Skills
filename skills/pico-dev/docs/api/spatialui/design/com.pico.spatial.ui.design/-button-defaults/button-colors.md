# buttonColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ButtonDefaults / buttonColors 
# buttonColors
```kotlin
@Composable
```fun  buttonColors ( ) :  ButtonColors 
Creates a default  ButtonColors  object with the accent color from the Pico theme as the container color and the on-accent color from the Pico theme as the content color. 
#### Return
A new  ButtonColors  object with the default colors. 
```kotlin
@Composable
```fun  buttonColors ( containerColor :  Color  =  Color.Unspecified ,  contentColor :  Color  =  Color.Unspecified ) :  ButtonColors 
Creates a  ButtonColors  that represents the default container and content colors used in a  Button . 
#### Parameters
container Color 
the container color of this  Button  when enabled. 
content Color 
the content color of this  Button  when enabled. its control the  Text 's color, and the  Icon 's tint