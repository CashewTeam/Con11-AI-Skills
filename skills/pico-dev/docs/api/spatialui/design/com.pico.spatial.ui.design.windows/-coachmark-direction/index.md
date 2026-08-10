# CoachmarkDirection | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design.windows / CoachmarkDirection 
# CoachmarkDirection
```kotlin
enum CoachmarkDirection : Enum<CoachmarkDirection>
```
CoachmarkDirection is used to specify the direction of the coachmark. 
Members Entries 
## Entries
ToStart 
```kotlin
ToStart
```
Display a coachmark to start of the anchor view. 
ToEnd 
```kotlin
ToEnd
```
Display a coachmark to end of the anchor view. 
Above 
```kotlin
Above
```
Display a coachmark above the anchor view. 
Below 
```kotlin
Below
```
Display a coachmark below the anchor view. 
## Properties
entries 
```kotlin
val entries: EnumEntries<CoachmarkDirection>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): CoachmarkDirection
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<CoachmarkDirection>
```
Returns an array containing the constants of this enum type, in the order they're declared.