# iconButtonSize | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / IconButtonDefaults / iconButtonSize 
# iconButtonSize
```kotlin
fun iconButtonSize(size: Dp): ButtonSize
```
Creates a  ButtonSize  that presents sizes used by  IconButton 
#### Return
The new  ButtonSize  with expected width and height 
#### Parameters
size 
the size of IconButton 
```kotlin
fun iconButtonSize(width: Dp, height: Dp): ButtonSize
```
Creates a  ButtonSize  that presents sizes used by  IconButton 
#### Return
The new  ButtonSize  with expected width and height 
#### Parameters
width 
IconButton's width 
height 
IconButton's height 
```kotlin
fun iconButtonSize(width: Dp = Dp.Unspecified, height: Dp = Dp.Unspecified, minWidth: Dp = Dp.Unspecified, maxWidth: Dp = Dp.Unspecified, minHeight: Dp = Dp.Unspecified, maxHeight: Dp = Dp.Unspecified): ButtonSize
```
Creates a  ButtonSize  that presents sizes used by  IconButton 
#### Return
a new  ButtonSize  with the given parameters. 
#### Parameters
width 
the width of this  ButtonSize . 
height 
the height of this  ButtonSize . 
min Width 
the minimum width of this  ButtonSize . 
max Width 
the maximum width of this  ButtonSize . 
min Height 
the minimum height of this  ButtonSize . 
max Height 
the maximum height of this  ButtonSize .