# CollisionDetectionMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / CollisionDetectionMode 
# CollisionDetectionMode
```kotlin
enum CollisionDetectionMode : Enum<CollisionDetectionMode>
```
Specifies the collision detection mode for a physics object. 
Collision detection can be performed in different ways depending on the required precision and computational cost. The modes range from discrete detection (the fastest but may allow missed collisions at high speeds) to speculative continuous detection (the most robust). 
Note: The collision detection system operates with a precision of 0.001 meters (1 millimeter). When the distance between the surfaces of two colliders is less than this threshold, the colliders are considered to be in contact. 
Members Entries 
## Entries
DISCRETE 
```kotlin
DISCRETE
```
Discrete collision detection. This mode has the following characteristics: 
CONTINUOUS 
```kotlin
CONTINUOUS
```
Continuous collision detection with static objects only. This mode has the following characteristics: 
CONTINUOUS_DYNAMIC 
```kotlin
CONTINUOUS_DYNAMIC
```
Continuous collision detection with both static and dynamic objects. This mode has the following characteristics: 
CONTINUOUS_SPECULATIVE 
```kotlin
CONTINUOUS_SPECULATIVE
```
Speculative continuous collision detection. This mode has the following characteristics: 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<CollisionDetectionMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The value of the CollisionDetectionMode. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): CollisionDetectionMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<CollisionDetectionMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.