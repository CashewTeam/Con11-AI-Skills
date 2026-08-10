# SpaceState | PICO Spatial SDK

core / com.pico.spatial.core.container / SpaceState 
# SpaceState
```kotlin
enum SpaceState : Enum<SpaceState>
```
Represents the types of spaces in which the application is currently running, including  UNKNOWN ,  SHARED_SPACE , and  FULL_SPACE . 
Members Entries 
## Entries
UNKNOWN 
```kotlin
UNKNOWN
```
Unable to determine which space the specified application is running in. 
SHARED_SPACE 
```kotlin
SHARED_SPACE
```
The specified application is running in a shared space. A shared space allows multiple applications to coexist in the same space. A shared space can only accommodate  WindowContainer s. 
FULL_SPACE 
```kotlin
FULL_SPACE
```
The specified application is running in a full space. A full space is exclusively occupied by a single application. When an application opens a  Stage , it will run in a full space. A full space can only accommodate the  Stage  (only one) and  WindowContainer s from the same application. 
## Properties
entries 
```kotlin
val entries: EnumEntries<SpaceState>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): SpaceState
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<SpaceState>
```
Returns an array containing the constants of this enum type, in the order they're declared.