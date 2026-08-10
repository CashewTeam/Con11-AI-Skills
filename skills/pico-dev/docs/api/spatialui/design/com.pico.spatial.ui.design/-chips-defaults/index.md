# ChipsDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ChipsDefaults 
# ChipsDefaults
```kotlin
object ChipsDefaults
```
the default values for chips. 
Members 
## Properties
Regular 
```kotlin
val Regular: ChipSize
```
The default size of regular chip. 
Small 
```kotlin
val Small: ChipSize
```
The default size of small chip. 
## Functions
chip Colors 
```kotlin
@Composable
```fun  chipColors ( ) :  ChipColors 
the default chip colors from the theme's color scheme. 
```kotlin
@Composable
```fun  chipColors ( contentColor :  Color  =  Color.Unspecified ,  backgroundColor :  Color  =  Color.Unspecified ) :  ChipColors 
Creates a new  ChipColors  instance with the specified content and background colors. If the colors are not specified, the default colors from the theme's color scheme are used. 
chip Size 
```kotlin
fun chipSize(height: Dp = Dp.Unspecified): ChipSize
```
Create a new  ChipSize  instance with expected height. 
toggleable Chip Colors 
```kotlin
@Composable
```fun  toggleableChipColors ( ) :  ToggleableChipColors 
the default toggleable chip colors from the theme's color scheme. 
```kotlin
@Composable
```fun  toggleableChipColors ( contentColor :  Color  =  Color.Unspecified ,  backgroundColor :  Color  =  Color.Unspecified ,  activeContentColor :  Color  =  Color.Unspecified ,  activeBackgroundColor :  Color  =  Color.Unspecified ) :  ToggleableChipColors 
Creates a new  ToggleableChipColors  instance with the specified content and background colors. If the colors are not specified, the default colors from the theme's color scheme are used.