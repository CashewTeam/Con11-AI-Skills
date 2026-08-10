# HeaderStyle | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / HeaderStyle 
# HeaderStyle
```kotlin
sealed class HeaderStyle
```
Define header style for  DatePicker . 
#### Inheritors
Dropdown Navigation Members 
## Constructors
Header Style 
```kotlin
protected constructor()
```
## Types
Dropdown 
```kotlin
object Dropdown : HeaderStyle
```
Dropdown style 
Navigation 
```kotlin
@Immutable
```class  Navigation ( val  yearSwitchable :  Boolean )  :  HeaderStyle 
Navigation style that can change year and month directly