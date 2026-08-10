# AudioInterpolatorType | PICO Spatial SDK

core / com.pico.spatial.core.ecs.audio / AudioInterpolatorType 
# AudioInterpolatorType
```kotlin
enum AudioInterpolatorType : Enum<AudioInterpolatorType>
```
AudioInterpolatorType is an enum that represents the fade type of how to fade the audio to the target volume during the fade operation by AudioPlayerController. 
Members Entries 
## Entries
CUBIC 
```kotlin
CUBIC
```
Cubic interpolation: S-shaped fade providing smooth acceleration and deceleration. 
LINEAR 
```kotlin
LINEAR
```
Linear interpolation: Smooth, constant-rate volume transition from start to target level. 
STEP 
```kotlin
STEP
```
Step interpolation: Immediate volume change at a specific time without fading. 
UNKNOWN 
```kotlin
UNKNOWN
```
Unknown interpolator type. 
## Properties
entries 
```kotlin
val entries: EnumEntries<AudioInterpolatorType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the interpolator type. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): AudioInterpolatorType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<AudioInterpolatorType>
```
Returns an array containing the constants of this enum type, in the order they're declared.