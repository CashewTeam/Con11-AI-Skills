# contentGap | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / contentGap 
# contentGap
```kotlin
fun ChipSize.contentGap(): Dp
```
Calculates the content gap for a given  ChipSize . 
#### Return
The content gap as a  Dp  value, which varies based on the  ChipSize . For  ChipsDefaults.Small , it returns 2.dp. For  ChipsDefaults.Regular , it returns 4.dp. For other sizes, it returns 0.dp.