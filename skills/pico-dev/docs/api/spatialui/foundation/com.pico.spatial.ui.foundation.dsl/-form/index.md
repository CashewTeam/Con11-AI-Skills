# Form | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.dsl / Form 
# Form
```kotlin
enum Form : Enum<Form>
```
Form of  WindowContainer . 
Members Entries 
## Entries
Automatic 
```kotlin
Automatic
```
The  WindowContainer 's form is determined by the system. 
Planar 
```kotlin
Planar
```
The  WindowContainer  behaves like a normal plane with default depth. 
Volumetric 
```kotlin
Volumetric
```
The  WindowContainer  allows defining its depth. 
## Properties
entries 
```kotlin
val entries: EnumEntries<Form>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Form
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Form>
```
Returns an array containing the constants of this enum type, in the order they're declared.