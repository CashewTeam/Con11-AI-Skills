# removeChipPadding | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / removeChipPadding 
# removeChipPadding
```kotlin
fun ChipSize.removeChipPadding(leading: Boolean = false): PaddingValues
```
Calculates the padding for a given  ChipSize  in  RemovableChip . 
#### Return
The padding as a  Dp  value, which varies based on the  ChipSize . 
#### Parameters
leading 
Whether the chip is leading or trailing. Defaults to false.