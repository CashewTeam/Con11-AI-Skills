# TitleAlignment | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / TitleAlignment 
# TitleAlignment
```kotlin
enum TitleAlignment : Enum<TitleAlignment>
```
Define how to place title in  TitleBar 
Members Entries 
## Entries
Center 
```kotlin
Center
```
Title will placed in the center of the space between left and right actions 
CenterInBar 
```kotlin
CenterInBar
```
Title will placed in the center of  TitleBar  and ignore the  TitleBar 's left and right actions 
## Properties
entries 
```kotlin
val entries: EnumEntries<TitleAlignment>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): TitleAlignment
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<TitleAlignment>
```
Returns an array containing the constants of this enum type, in the order they're declared.