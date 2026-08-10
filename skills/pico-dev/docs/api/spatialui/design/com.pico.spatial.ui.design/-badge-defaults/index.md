# BadgeDefaults | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / BadgeDefaults 
# BadgeDefaults
```kotlin
object BadgeDefaults
```
The default values for the  Badge  component. 
Members 
## Properties
Dot Color 
```kotlin
@get:Composable
```val  DotColor :  Color 
the default dot color 
Dot Size 
```kotlin
val DotSize: Dp
```
the default dot size 
Extra Small 
```kotlin
val ExtraSmall: BadgeSize
```
the default extraSmall size of badge 
Number Regular 
```kotlin
val NumberRegular: BadgeSize
```
the default regular size of number badge 
Number Small 
```kotlin
val NumberSmall: BadgeSize
```
the default small size of number badge 
Number Text Style 
```kotlin
@get:Composable
```val  NumberTextStyle :  TextStyle 
the default text style of number badge 
Regular 
```kotlin
val Regular: BadgeSize
```
the default regular size of badge 
Small 
```kotlin
val Small: BadgeSize
```
the default small size of badge 
## Functions
badge Colors 
```kotlin
@Composable
```fun  badgeColors ( ) :  BadgeColors 
default colors for badge 
```kotlin
@Composable
```fun  badgeColors ( backgroundColor :  Color  =  Color.Unspecified ,  contentColor :  Color  =  Color.Unspecified ) :  BadgeColors 
Create a  BadgeColors  with expected background color and content color. 
badge Size 
```kotlin
fun badgeSize(width: Dp = Dp.Unspecified, height: Dp = Dp.Unspecified): BadgeSize
```
Create a  BadgeSize  with expected width and height. 
number Badge Colors 
```kotlin
@Composable
```fun  numberBadgeColors ( ) :  BadgeColors 
default colors for number badge