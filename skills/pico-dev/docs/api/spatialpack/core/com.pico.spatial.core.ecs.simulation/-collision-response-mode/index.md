# CollisionResponseMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / CollisionResponseMode 
# CollisionResponseMode
```kotlin
enum CollisionResponseMode : Enum<CollisionResponseMode>
```
Defines how collision interactions are handled for an entity, including the level of data collected and whether physical collision effects are applied. 
Note: The collision detection system operates with a precision of 0.001 meters (1 millimeter). When the distance between the surfaces of two colliders is less than this threshold, the colliders are considered to be in contact. 
Members Entries 
## Entries
TRIGGER_FULL 
```kotlin
TRIGGER_FULL
```
Collects detailed collision data, including contact points, normal vectors, and penetration depths; but does  not  apply any physical collision effects to the entity. Useful for detecting precise interactions without affecting simulation behavior. 
TRIGGER_LITE 
```kotlin
TRIGGER_LITE
```
Collects minimal collision data (contact points only) without applying physical collision effects. Suitable for lightweight trigger-based interactions. 
COLLIDER_FULL 
```kotlin
COLLIDER_FULL
```
Collects detailed collision data, including contact points, normal vectors, and penetration depths; and applies physical collision effects to the entity. Use this mode when the entity should physically respond to collisions. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<CollisionResponseMode>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The value of the CollisionResponseMode. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): CollisionResponseMode
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<CollisionResponseMode>
```
Returns an array containing the constants of this enum type, in the order they're declared.