# colors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / SegmentControlDefaults / colors 
# colors
```kotlin
@Composable
```fun  colors ( ) :  SegmentControlColors 
the default colors for the segment control. 
#### Return
The default colors for the segment control. 
```kotlin
@Composable
```fun  colors ( itemBackgroundColor :  Color  =  Color.Unspecified ,  itemContentColor :  Color  =  Color.Unspecified ,  selectedItemBackgroundColor :  Color  =  Color.Unspecified ,  selectedItemContentColor :  Color  =  Color.Unspecified ) :  SegmentControlColors 
Creates a new  SegmentControlColors  instance with the specified container color, content color, and selected content color. If the colors are not specified, the default colors from the color scheme will be used. 
#### Return
A new  SegmentControlColors  instance with the specified container color, content color, and selected content color. 
#### Parameters
item Background Color 
The color to be used for the unchecked item background. 
item Content Color 
The color to be used for the unchecked item content. 
selected Item Background Color 
The color to be used for the checked item background. 
selected Item Content Color 
The color to be used for the checked item content.