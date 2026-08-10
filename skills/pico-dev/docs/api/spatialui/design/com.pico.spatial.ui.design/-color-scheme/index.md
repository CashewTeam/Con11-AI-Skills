# ColorScheme | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / ColorScheme 
# ColorScheme
```kotlin
@Immutable
```class  ColorScheme ( val  fillPrimary :  Color ,  val  fillSecondary :  Color ,  val  fillTertiary :  Color ,  val  fillLight :  Color ,  val  labelPrimaryLight :  Color ,  val  labelPrimary :  Color ,  val  labelSecondary :  Color ,  val  labelTertiary :  Color ,  val  labelQuaternary :  Color ,  val  lightenHover :  Color ,  val  lightenPressed :  Color ,  val  error :  Color ,  val  alert :  Color ,  val  passable :  Color ,  val  interaction :  Color ,  val  dividerLine :  Color ) 
A color scheme holds all the named color roles parameters for PICO design system. 
Members 
## Constructors
Color Scheme 
```kotlin
constructor(fillPrimary: Color, fillSecondary: Color, fillTertiary: Color, fillLight: Color, labelPrimaryLight: Color, labelPrimary: Color, labelSecondary: Color, labelTertiary: Color, labelQuaternary: Color, lightenHover: Color, lightenPressed: Color, error: Color, alert: Color, passable: Color, interaction: Color, dividerLine: Color)
```
## Properties
alert 
```kotlin
val alert: Color
```
Alert semantic color. 
divider Line 
```kotlin
val dividerLine: Color
```
Divider line color. 
error 
```kotlin
val error: Color
```
Error semantic color. 
fill Light 
```kotlin
val fillLight: Color
```
Light background color. 
fill Primary 
```kotlin
val fillPrimary: Color
```
Background color for small areas and important elements. 
fill Secondary 
```kotlin
val fillSecondary: Color
```
Background color for large areas and non-important elements. 
fill Tertiary 
```kotlin
val fillTertiary: Color
```
Background color for the least important elements. 
interaction 
```kotlin
val interaction: Color
```
Interaction semantic color. 
label Primary 
```kotlin
val labelPrimary: Color
```
Primary content color. 
label Primary Light 
```kotlin
val labelPrimaryLight: Color
```
The foreground color used on  fillPrimary . 
label Quaternary 
```kotlin
val labelQuaternary: Color
```
Quaternary content color. 
label Secondary 
```kotlin
val labelSecondary: Color
```
Secondary content color. 
label Tertiary 
```kotlin
val labelTertiary: Color
```
Tertiary content color. 
lighten Hover 
```kotlin
val lightenHover: Color
```
Hover overlay color. 
lighten Pressed 
```kotlin
val lightenPressed: Color
```
Pressed overlay color. 
passable 
```kotlin
val passable: Color
```
Passable semantic color. 
## Functions
copy 
```kotlin
fun copy(fillPrimary: Color = this.fillPrimary, fillSecondary: Color = this.fillSecondary, fillTertiary: Color = this.fillTertiary, fillLight: Color = this.fillLight, labelPrimaryLight: Color = this.labelPrimaryLight, labelPrimary: Color = this.labelPrimary, labelSecondary: Color = this.labelSecondary, labelTertiary: Color = this.labelTertiary, labelQuaternary: Color = this.labelQuaternary, lightenHover: Color = this.lightenHover, lightenPressed: Color = this.lightenPressed, error: Color = this.error, alert: Color = this.alert, passable: Color = this.passable, interaction: Color = this.interaction, dividerLine: Color = this.dividerLine): ColorScheme
```to String 
```kotlin
open override fun toString(): String
```