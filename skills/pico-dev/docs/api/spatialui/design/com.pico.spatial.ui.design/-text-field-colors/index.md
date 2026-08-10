# TextFieldColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / TextFieldColors 
# TextFieldColors
```kotlin
@Immutable
```class  TextFieldColors 
Defines  TextField  color theme 
#### Parameters
text Color 
color for editable text 
background Color 
color for background 
focused Color 
color for background when focused 
placeholder Color 
color for placeholder text 
error Color 
color for error tips 
Members 
## Properties
background Color 
```kotlin
val backgroundColor: Color
```error Color 
```kotlin
val errorColor: Color
```focused Color 
```kotlin
val focusedColor: Color
```placeholder Color 
```kotlin
val placeholderColor: Color
```text Color 
```kotlin
val textColor: Color
```
## Functions
copy 
```kotlin
fun copy(textColor: Color = this.textColor, backgroundColor: Color = this.backgroundColor, focusedColor: Color = this.focusedColor, placeholderColor: Color = this.placeholderColor, errorColor: Color = this.errorColor): TextFieldColors
```
copy to a new instance 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```