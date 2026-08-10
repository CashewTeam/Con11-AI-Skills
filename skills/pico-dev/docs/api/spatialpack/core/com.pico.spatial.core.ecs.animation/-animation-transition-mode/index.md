# AnimationTransitionMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / AnimationTransitionMode 
# AnimationTransitionMode
```kotlin
enum AnimationTransitionMode : Enum<AnimationTransitionMode>
```
The transition mode the play animation method performs between a current animation and a new animation. 
Members Entries 
## Entries
DEFAULT 
```kotlin
DEFAULT
```
The default behavior is that for playing skeletal animations, the CROSSFADE mode will be used, while for other animations, the COMPOSE mode will be used. 
CROSSFADE 
```kotlin
CROSSFADE
```
Smoothly transitions from the current animation to the new animation over a specified transition duration. 
COMPOSE 
```kotlin
COMPOSE
```
Directly adding a new animation run has no impact on the current animation. 
STOP_AND_CROSSFADE 
```kotlin
STOP_AND_CROSSFADE
```
Stops the current animation and uses the current value of that animation as the blend value for the transition to the new animation. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<AnimationTransitionMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the transition mode. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): AnimationTransitionMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<AnimationTransitionMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.