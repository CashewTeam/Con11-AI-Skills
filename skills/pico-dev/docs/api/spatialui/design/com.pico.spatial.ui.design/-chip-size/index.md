# ChipSize | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ChipSize 
# ChipSize
```kotlin
@JvmInline
```value  class  ChipSize 
size for  Chip 
#### Parameters
height 
height of chip 
Members Members & Extensions 
## Properties
height 
```kotlin
val height: Dp
```
## Functions
content Gap 
```kotlin
fun ChipSize.contentGap(): Dp
```
Calculates the content gap for a given  ChipSize . 
content Padding 
```kotlin
fun ChipSize.contentPadding(leading: Boolean = false): PaddingValues
```
Calculates the content padding for a given  ChipSize . 
corner Radius 
```kotlin
fun ChipSize.cornerRadius(): Dp
```
Calculates the corner radius for a given  ChipSize . 
remove Chip Icon Size 
```kotlin
fun ChipSize.removeChipIconSize(): Dp
```
Calculates the icon size for a given  ChipSize  in  RemovableChip . 
remove Chip Padding 
```kotlin
fun ChipSize.removeChipPadding(leading: Boolean = false): PaddingValues
```
Calculates the padding for a given  ChipSize  in  RemovableChip . 
text Style 
```kotlin
@Composable
```fun  ChipSize . textStyle ( ) :  TextStyle 
Calculates the text style for a given  ChipSize .