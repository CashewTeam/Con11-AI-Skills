# AmbientOrientationMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AmbientOrientationMode 
# AmbientOrientationMode
```kotlin
enum AmbientOrientationMode : Enum<AmbientOrientationMode>
```
Defines how ambient audio orientation is applied to the audio source. 
Members Entries 
## Entries
INVALID 
```kotlin
INVALID
```
Invalid ambient orientation mode. 
POSITION_AND_ORIENTATION 
```kotlin
POSITION_AND_ORIENTATION
```
The ambient effect depends on both the source/listener position and orientation. This creates a more spatially-aware audio experience. 
ORIENTATION_ONLY 
```kotlin
ORIENTATION_ONLY
```
The ambient effect depends only on the source/listener orientation, ignoring positional differences. This is the default mode. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<AmbientOrientationMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): AmbientOrientationMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<AmbientOrientationMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.