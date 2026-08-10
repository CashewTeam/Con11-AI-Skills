# listItemColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ListItemDefaults / listItemColors 
# listItemColors
```kotlin
@Composable
```fun  listItemColors ( ) :  ListItemColors 
Provide default  ListItemColors  for  ListItem 
#### Return
default  ListItemColors 
```kotlin
@Composable
```fun  listItemColors ( backgroundColor :  Color  =  Color.Unspecified ,  leadingColor :  Color  =  Color.Unspecified ,  headlineColor :  Color  =  Color.Unspecified ,  supportingColor :  Color  =  Color.Unspecified ,  trailingColor :  Color  =  Color.Unspecified ) :  ListItemColors 
Create a custom  ListItemColors  for  ListItem 
#### Return
a new  ListItemColors  with expected colors. See parameter list for color list. 
#### Parameters
background Color 
for background shape color 
leading Color 
leading content color, such as icon & text color 
headline Color 
headline content color, usually is for text color 
supporting Color 
supporting content color, usually is for text color 
trailing Color 
trailing content color, such as icon & text color