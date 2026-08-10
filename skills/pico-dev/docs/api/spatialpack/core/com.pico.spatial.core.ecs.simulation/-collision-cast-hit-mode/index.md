# CollisionCastHitMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / CollisionCastHitMode 
# CollisionCastHitMode
```kotlin
enum CollisionCastHitMode : Enum<CollisionCastHitMode>
```
Specifies the mode for reporting hits in a collision cast query. 
This enum determines whether a ray cast or convex cast should return only the closest hit or all hits along its path. 
Members Entries 
## Entries
NEAREST 
```kotlin
NEAREST
```
Reports only the closest hit point to the cast origin. 
ALL 
```kotlin
ALL
```
Reports all hit points along the cast path. 
## Properties
entries 
```kotlin
val entries: EnumEntries<CollisionCastHitMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): CollisionCastHitMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<CollisionCastHitMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.