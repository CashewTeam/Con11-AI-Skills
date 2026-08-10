# DistanceAttenuationMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / DistanceAttenuationMode 
# DistanceAttenuationMode
```kotlin
enum DistanceAttenuationMode : Enum<DistanceAttenuationMode>
```
Defines how audio volume attenuates as the distance from the audio source increases. 
Members Entries 
## Entries
FIXED 
```kotlin
FIXED
```
The volume remains constant, playing at a fixed level regardless of the listener’s distance from the audio source. 
INVERSE_SQUARED 
```kotlin
INVERSE_SQUARED
```
The volume decreases according to the inverse square law, dropping rapidly with increasing distance to mimic natural sound propagation. This is the default mode. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<DistanceAttenuationMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the attenuation mode. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): DistanceAttenuationMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<DistanceAttenuationMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.