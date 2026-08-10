# NumberFieldColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / NumberFieldColors 
# NumberFieldColors
```kotlin
@Immutable
```class  NumberFieldColors 
The colors for  NumberField . 
#### Parameters
content Color 
The color of the text. 
background Color 
The color of the background. 
focused Color 
The color of the background when focused. 
error Color 
The color of the background when error. 
Members 
## Properties
background Color 
```kotlin
val backgroundColor: Color
```content Color 
```kotlin
val contentColor: Color
```error Color 
```kotlin
val errorColor: Color
```focused Color 
```kotlin
val focusedColor: Color
```
## Functions
copy 
```kotlin
fun copy(contentColor: Color = this.contentColor, backgroundColor: Color = this.backgroundColor, focusedColor: Color = this.focusedColor, errorColor: Color = this.errorColor): NumberFieldColors
```
copy to a new instance 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```