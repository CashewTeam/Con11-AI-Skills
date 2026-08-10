# LookAtForwardDirection | PICO Spatial SDK

core / com.pico.spatial.core.ecs / LookAtForwardDirection 
# LookAtForwardDirection
```kotlin
enum LookAtForwardDirection : Enum<LookAtForwardDirection>
```
Enumeration defining possible forward direction axes for the  LookAtComponent  in 3D spatial simulation. Specifies which axis an entity should use as its forward direction when implementing "look at" behavior. 
Members Entries 
## Entries
POSITIVE_Z 
```kotlin
POSITIVE_Z
```
Represents the positive Z-axis as the forward direction vector 
NEGATIVE_Z 
```kotlin
NEGATIVE_Z
```
Represents the negative Z-axis as the forward direction vector 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<LookAtForwardDirection>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The integer value of the forward direction. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): LookAtForwardDirection
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<LookAtForwardDirection>
```
Returns an array containing the constants of this enum type, in the order they're declared.