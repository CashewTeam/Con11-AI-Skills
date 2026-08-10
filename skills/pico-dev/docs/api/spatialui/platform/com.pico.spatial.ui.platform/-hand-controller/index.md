# HandController | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / HandController 
# HandController
```kotlin
enum HandController : Enum<HandController>
```
hand controller type in Pico OS, provide 
- 
Left 
- 
Right 
- 
Unknown 
Members Entries 
## Entries
Left 
```kotlin
Left
```
left hand controller 
Right 
```kotlin
Right
```
right hand controller 
Unknown 
```kotlin
Unknown
```
unknown hand controller 
## Properties
entries 
```kotlin
val entries: EnumEntries<HandController>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): HandController
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<HandController>
```
Returns an array containing the constants of this enum type, in the order they're declared.