# InteractionKind | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture.data / InteractionKind 
# InteractionKind
```kotlin
enum InteractionKind : Enum<InteractionKind>
```
InteractionKind is used to describe the kind of interaction that is currently being performed. 
Members Entries 
## Entries
Unknown 
```kotlin
Unknown
```
unknown interaction kind 
DirectPinch 
```kotlin
DirectPinch
```
Direct pinch 
Poke 
```kotlin
Poke
```
Poke 
GazePinch 
```kotlin
GazePinch
```
Gaze pinch 
RayBasedPinch 
```kotlin
RayBasedPinch
```
Ray based pinch 
Pointer 
```kotlin
Pointer
```
Pointer 
## Properties
entries 
```kotlin
val entries: EnumEntries<InteractionKind>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): InteractionKind
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<InteractionKind>
```
Returns an array containing the constants of this enum type, in the order they're declared.