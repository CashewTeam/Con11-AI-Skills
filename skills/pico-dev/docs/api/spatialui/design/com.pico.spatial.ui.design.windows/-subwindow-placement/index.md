# SubwindowPlacement | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / SubwindowPlacement 
# SubwindowPlacement
```kotlin
enum SubwindowPlacement : Enum<SubwindowPlacement>
```
Determines the placement of the subwindow. 
Members Entries 
## Entries
Default 
```kotlin
Default
```
Determined by the current layout direction. Left if layout direction is LTR, right if layout direction is RTL. 
Left 
```kotlin
Left
```
Will be placed on the left side of the window container. 
Right 
```kotlin
Right
```
Will be placed on the right side of the window container. 
## Properties
entries 
```kotlin
val entries: EnumEntries<SubwindowPlacement>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): SubwindowPlacement
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<SubwindowPlacement>
```
Returns an array containing the constants of this enum type, in the order they're declared.