# textStyle | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / textStyle 
# textStyle
```kotlin
@Composable
```fun  ChipSize . textStyle ( ) :  TextStyle 
Calculates the text style for a given  ChipSize . 
#### Return
The text style as a  TextStyle  value, which varies based on the  ChipSize . For  ChipsDefaults.Small , it returns PicoTheme.typography.labelMedium. For  ChipsDefaults.Regular , it returns PicoTheme.typography.labelLarge. For other sizes, it returns PicoTheme.typography.labelLarge. 
```kotlin
@Composable
```fun  SegmentControlSize . textStyle ( ) :  TextStyle 
The text style of the segment control item. 
- 
#### Return
The text style of the segment control item.