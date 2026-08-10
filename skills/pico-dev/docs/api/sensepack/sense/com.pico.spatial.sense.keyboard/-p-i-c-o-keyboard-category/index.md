# PICOKeyboardCategory | PICO Spatial SDK

sense / com.pico.spatial.sense.keyboard / PICOKeyboardCategory 
# PICOKeyboardCategory
```kotlin
enum PICOKeyboardCategory : Enum<PICOKeyboardCategory>
```
Represents the category of a tracked PICO keyboard anchor. 
Members Entries 
## Entries
UNKNOWN 
```kotlin
UNKNOWN
```
Unknown or reserved category. 
KEYBOARD 
```kotlin
KEYBOARD
```
Physical keyboard device. 
TOUCHPAD 
```kotlin
TOUCHPAD
```
Touchpad device. 
## Properties
entries 
```kotlin
val entries: EnumEntries<PICOKeyboardCategory>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the category. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): PICOKeyboardCategory
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<PICOKeyboardCategory>
```
Returns an array containing the constants of this enum type, in the order they're declared.