# KinematicCollisionReportMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / KinematicCollisionReportMode 
# KinematicCollisionReportMode
```kotlin
enum KinematicCollisionReportMode : Enum<KinematicCollisionReportMode>
```
Defines whether the collision will be reported when the current kinematic object is colliding with other static or kinematic objects. 
Note: The collision detection system operates with a precision of 0.001 meters (1 millimeter). When the distance between the surfaces of two colliders is less than this threshold, the colliders are considered to be in contact. 
Members Entries 
## Entries
NONE 
```kotlin
NONE
```
Does not report any collisions for the current kinematic object. 
WITH_STATIC_ONLY 
```kotlin
WITH_STATIC_ONLY
```
Reports collisions only with static objects for the current kinematic object. 
WITH_KINEMATIC_ONLY 
```kotlin
WITH_KINEMATIC_ONLY
```
Reports collisions only with other kinematic objects for the current kinematic object. 
ALL 
```kotlin
ALL
```
Reports all collisions regardless of the rigid body mode of the other object for the current kinematic object. 
## Properties
entries 
```kotlin
val entries: EnumEntries<KinematicCollisionReportMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): KinematicCollisionReportMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<KinematicCollisionReportMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.