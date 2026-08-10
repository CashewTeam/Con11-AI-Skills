# contentPadding | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / contentPadding 
# contentPadding
```kotlin
fun ChipSize.contentPadding(leading: Boolean = false): PaddingValues
```
Calculates the content padding for a given  ChipSize . 
#### Return
The content padding as a  PaddingValues  object, which varies based on the  ChipSize . For  ChipsDefaults.Small , it returns horizontal padding of 8.dp. For  ChipsDefaults.Regular , it returns horizontal padding of 12.dp. For other sizes, it returns horizontal padding of 16.dp.