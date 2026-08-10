# SegmentControlDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / SegmentControlDefaults 
# SegmentControlDefaults
```kotlin
object SegmentControlDefaults
```
Provides default values for the  SegmentControl  composable function. 
Members 
## Properties
background Color 
```kotlin
@get:Composable
```val  backgroundColor :  Color 
The background color of the segment control. 
Container Padding 
```kotlin
val ContainerPadding: Dp
```
The padding value of the segment control. 
Item Gap 
```kotlin
val ItemGap: Dp
```
the gap between icon and text in the item. 
Item Space 
```kotlin
val ItemSpace: Dp
```
The space between items in the segment control. 
Regular 
```kotlin
val Regular: SegmentControlSize
```
The regular size of a segment control item. 
Rich 
```kotlin
val Rich: SegmentControlSize
```
The size of a segment control item in RichSegmentControl. 
Small 
```kotlin
val Small: SegmentControlSize
```
The small size of a segment control item. 
## Functions
colors 
```kotlin
@Composable
```fun  colors ( ) :  SegmentControlColors 
the default colors for the segment control. 
```kotlin
@Composable
```fun  colors ( itemBackgroundColor :  Color  =  Color.Unspecified ,  itemContentColor :  Color  =  Color.Unspecified ,  selectedItemBackgroundColor :  Color  =  Color.Unspecified ,  selectedItemContentColor :  Color  =  Color.Unspecified ) :  SegmentControlColors 
Creates a new  SegmentControlColors  instance with the specified container color, content color, and selected content color. If the colors are not specified, the default colors from the color scheme will be used. 
segment Control Size 
```kotlin
fun segmentControlSize(height: Dp = Dp.Unspecified): SegmentControlSize
```
Creates a  SegmentControlSize  instance with specified height. This function allows you to customize the size of a segment control by providing custom height values. If no values are provided, it uses  Dp.Unspecified .