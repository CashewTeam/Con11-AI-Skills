# cornerRadius | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / cornerRadius 
# cornerRadius
```kotlin
fun ChipSize.cornerRadius(): Dp
```
Calculates the corner radius for a given  ChipSize . 
#### Return
The corner radius as a  Dp  value, which varies based on the  ChipSize . For  ChipsDefaults.Small , it returns 12.dp. For  ChipsDefaults.Regular , it returns 16.dp. For other sizes, it returns half of the chip's height.