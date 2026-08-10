# RepeatMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / RepeatMode 
# RepeatMode
```kotlin
enum RepeatMode : Enum<RepeatMode>
```
Controls how an animation behaves when it reaches the end. The animation's repeat count must be set to a positive integer or '-1' for this property to have an effect. 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
The animation will not repeat. 
RESTART 
```kotlin
RESTART
```
To restart the animation from the beginning when it reaches the end. 
REVERSE 
```kotlin
REVERSE
```
To restart the animation reversely when its current playback ends. For example, if the repeat count is set to  3 , the animation will be played three times in the following way: 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<RepeatMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The stable integer value of the repeat mode. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): RepeatMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<RepeatMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.