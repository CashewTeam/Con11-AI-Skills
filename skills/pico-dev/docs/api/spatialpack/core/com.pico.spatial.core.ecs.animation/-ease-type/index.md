# EaseType | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / EaseType 
# EaseType
```kotlin
enum EaseType : Enum<EaseType>
```
Provides functions or algorithms used for animation interpolation, which are used to control the rate of change of an animation object over the timeline. 
Members Entries 
## Entries
LINEAR 
```kotlin
LINEAR
```
A constant rate of change throughout the animation over the timeline. 
EASE_IN 
```kotlin
EASE_IN
```
The rate of change gradually increases over the timeline, causing the animation to start quite slowly and then gradually accelerate. 
EASE_OUT 
```kotlin
EASE_OUT
```
The rate of change gradually decreases over the timeline, causing the animation to start quite fast and then gradually slow down. 
EASE_INOUT 
```kotlin
EASE_INOUT
```
Combines the effects of both ease-in and ease-out modes, resulting in an animation that starts quite slowly, gradually accelerates in the middle, and gradually slows down toward the end. 
EASE_IN_CUBIC 
```kotlin
EASE_IN_CUBIC
```
Provides a cubic ease-in effect, causing the animation to start very slowly and accelerate more sharply than the ease-in mode. 
EASE_OUT_CUBIC 
```kotlin
EASE_OUT_CUBIC
```
Provides a cubic ease-out effect, causing the animation to start very fast and slow down more sharply than the ease-out mode. 
EASE_INOUT_CUBIC 
```kotlin
EASE_INOUT_CUBIC
```
Combines the effects of both cubic ease-in and cubic ease-out modes, resulting in an animation that starts very slowly, accelerates in the middle more sharply, and slows down toward the end more sharply. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<EaseType>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The stable integer value of the ease type. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): EaseType
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<EaseType>
```
Returns an array containing the constants of this enum type, in the order they're declared.