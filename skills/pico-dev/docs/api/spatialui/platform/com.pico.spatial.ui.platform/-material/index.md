# Material | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / Material 
# Material
```kotlin
enum Material : Enum<Material>
```
Material in PICO design system is made up of two colors with blend mode. 
Members Entries 
## Entries
None 
```kotlin
None
```
No material. 
Regular 
```kotlin
Regular
```
The  Material  of the base layer e.g：Window、Augment、Tab Bar、Tool Bar 
Thick 
```kotlin
Thick
```
The  Material  of the elevated layer that occupy a large area e.g：Dialog Alert、Sheet、Menu 
Thickest 
```kotlin
Thickest
```
The  Material  of the elevated layer that occupy a small area e.g：Tooltip、Text Selector 
Thin 
```kotlin
Thin
```
The  Material  of the elevated layer that occupy a small area e.g：Box、Button、CheckBox. Currently, It has no effect for the Window. 
## Properties
entries 
```kotlin
val entries: EnumEntries<Material>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Material
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Material>
```
Returns an array containing the constants of this enum type, in the order they're declared.