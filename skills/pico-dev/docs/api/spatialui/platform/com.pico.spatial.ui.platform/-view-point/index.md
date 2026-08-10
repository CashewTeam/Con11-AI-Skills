# ViewPoint | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / ViewPoint 
# ViewPoint
```kotlin
enum ViewPoint : Enum<ViewPoint>
```
The ViewPoint enum. 
Members Entries 
## Entries
Front 
```kotlin
Front
```
The front of volume. Corresponding value is 0. 
Right 
```kotlin
Right
```
The right of volume. Corresponding value is 1. 
Back 
```kotlin
Back
```
The back of volume. Corresponding value is 2. 
Left 
```kotlin
Left
```
The left of volume. Corresponding value is 3. 
## Types
Companion 
```kotlin
object Companion
```
Holds helpful values about  ViewPoint . 
## Properties
entries 
```kotlin
val entries: EnumEntries<ViewPoint>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The value of the ViewPoint. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): ViewPoint
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<ViewPoint>
```
Returns an array containing the constants of this enum type, in the order they're declared.