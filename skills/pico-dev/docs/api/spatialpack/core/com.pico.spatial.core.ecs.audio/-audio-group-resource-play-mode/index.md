# AudioGroupResourcePlayMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioGroupResourcePlayMode 
# AudioGroupResourcePlayMode
```kotlin
enum AudioGroupResourcePlayMode : Enum<AudioGroupResourcePlayMode>
```
Audio group resource play mode. 
Defines the playback order for audio resources within an audio group. This is a Kotlin wrapper for the Java AudioGroupResourcePlayMode enum. 
Members Entries 
## Entries
RANDOM 
```kotlin
RANDOM
```
Random selection mode. Audio resources will be played in random order. 
FORWARD 
```kotlin
FORWARD
```
Forward sequence mode. Audio resources will be played in the order they were added (default mode). 
BACKWARD 
```kotlin
BACKWARD
```
Backward sequence mode. Audio resources will be played in reverse order. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility.* 
## Properties
entries 
```kotlin
val entries: EnumEntries<AudioGroupResourcePlayMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): AudioGroupResourcePlayMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<AudioGroupResourcePlayMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.