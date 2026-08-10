# Vibrant | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.vibrant / Vibrant 
# Vibrant
```kotlin
enum Vibrant : Enum<Vibrant>
```
Vibrant styles. 
Members Members & Extensions Entries 
## Entries
Darkest 
```kotlin
Darkest
```
Darkest vibrant style. 
UltraDark 
```kotlin
UltraDark
```
Ultra dark vibrant style. 
Darker 
```kotlin
Darker
```
Darker vibrant style. 
Semidark 
```kotlin
Semidark
```
Semidark vibrant style. 
Dark 
```kotlin
Dark
```
Dark vibrant style. 
Neutral 
```kotlin
Neutral
```
Neutral vibrant style. 
Light 
```kotlin
Light
```
Light vibrant style. 
SemiLight 
```kotlin
SemiLight
```
Semilight vibrant style. 
UltraLight 
```kotlin
UltraLight
```
Ultralight vibrant style. 
LightenPressed 
```kotlin
LightenPressed
```
Lighten pressed vibrant style. 
None 
```kotlin
None
```
None vibrant style.  Vibrant.None  can be used to disable vibrant effect. 
Unspecified 
```kotlin
Unspecified
```
Unspecified means that the vibrant style is not specified. When use  Vibrant.Unspecified , the vibrant effect will be inherited from parent effect. 
## Properties
entries 
```kotlin
val entries: EnumEntries<Vibrant>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
take Or Else 
```kotlin
inline fun Vibrant.takeOrElse(block: () -> Vibrant): Vibrant
```
Return the specified vibrant style if it is specified, otherwise return the default vibrant style. 
value Of 
```kotlin
fun valueOf(value: String): Vibrant
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Vibrant>
```
Returns an array containing the constants of this enum type, in the order they're declared.