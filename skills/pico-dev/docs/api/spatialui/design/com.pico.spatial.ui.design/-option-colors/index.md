# OptionColors | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / OptionColors 
# OptionColors
```kotlin
@Immutable
```class  OptionColors 
The colors used by  Option 
Members 
## Properties
checked Container Color 
```kotlin
val checkedContainerColor: Color
```
The background color when option is checked 
checked Content Color 
```kotlin
val checkedContentColor: Color
```
The content color when option is checked 
un Checked Container Color 
```kotlin
val unCheckedContainerColor: Color
```
The background color when option is unchecked 
un Checked Content Color 
```kotlin
val unCheckedContentColor: Color
```
The content color when option is unchecked 
## Functions
copy 
```kotlin
fun copy(checkedContainerColor: Color = this.checkedContainerColor, checkedContentColor: Color = this.checkedContentColor, unCheckedContainerColor: Color = this.unCheckedContainerColor, unCheckedContentColor: Color = this.unCheckedContentColor): OptionColors
```
Copy a new  OptionColors  instance from current with the given parameters applied. 
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```