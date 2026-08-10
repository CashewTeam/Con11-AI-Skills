# SlerpPath | PICO Spatial SDK

foundation / com.pico.spatial.core.math / Rotation / Companion / SlerpPath 
# SlerpPath
```kotlin
enum SlerpPath : Enum<Rotation.Companion.SlerpPath>
```
Defines the arc path for Spherical Linear Interpolation (Slerp). 
Members Entries 
## Entries
SHORTEST 
```kotlin
SHORTEST
```
Interpolates along the shorter arc between the two rotations. 
LONGEST 
```kotlin
LONGEST
```
Interpolates along the longer arc between the two rotations. 
## Properties
entries 
```kotlin
val entries: EnumEntries<Rotation.Companion.SlerpPath>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): Rotation.Companion.SlerpPath
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<Rotation.Companion.SlerpPath>
```
Returns an array containing the constants of this enum type, in the order they're declared.