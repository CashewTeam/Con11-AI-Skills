# scrollIndicatorColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ScrollIndicatorDefaults / scrollIndicatorColors 
# scrollIndicatorColors
```kotlin
@Stable
```@ Composable fun  scrollIndicatorColors ( ) :  ScrollIndicatorColors 
Provide default  ScrollIndicatorColors  for  ScrollIndicator 
#### Return
default  ScrollIndicatorColors 
```kotlin
@Stable
```@ Composable fun  scrollIndicatorColors ( trackColor :  Color  =  Color.Unspecified ,  indicatorColor :  Color  =  Color.Unspecified ,  scrollMarksColor :  Color  =  Color.Unspecified ,  backgroundColor :  Color  =  Color.Unspecified ) :  ScrollIndicatorColors 
Customize  ScrollIndicatorColors  used for  ScrollIndicator . 
#### Return
The new  ScrollIndicatorColors  instance with expected indicatorColor and backgroundColor. 
#### Parameters
track Color 
The color of the track. 
indicator Color 
The color of the indicator. 
scroll Marks Color 
The color of the scrollingMarks. 
background Color 
The color of the background.