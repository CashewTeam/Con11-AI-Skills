# CollisionInfoDetailLevel | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / CollisionInfoDetailLevel 
# CollisionInfoDetailLevel
```kotlin
enum CollisionInfoDetailLevel : Enum<CollisionInfoDetailLevel>
```
The enum class that defines what kind of information will be included when a collision object reports this collision event. 
Note: The collision detection system operates with a precision of 0.001 meters (1 millimeter). When the distance between the surfaces of two colliders is less than this threshold, the colliders are considered to be in contact. 
Members Entries 
## Entries
BRIEF 
```kotlin
BRIEF
```
Reports brief collision information with dynamic collision objects, including averaged position of contacts, accumulated impulse of contacts, and maximum penetrationDistance among contacts. Information of each contact point is  not  provided. 
DETAILED 
```kotlin
DETAILED
```
Reports detailed collision information with dynamic collision objects. Besides information from  CollisionInfoDetailLevel.BRIEF , it also includes detailed data of all contact points, including their position, normal, impulse, and penetrationDistance. 
UNKNOWN 
```kotlin
UNKNOWN
```
Reserved value for forward compatibility. 
## Properties
entries 
```kotlin
val entries: EnumEntries<CollisionInfoDetailLevel>
```
Returns a representation of an immutable list of all enum entries, in the order they're declared. 
value 
```kotlin
val value: Int
```
The value of the CollisionInfoDetailLevel. 
## Functions
value Of 
```kotlin
fun valueOf(value: String): CollisionInfoDetailLevel
```
Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) 
values 
```kotlin
fun values(): Array<CollisionInfoDetailLevel>
```
Returns an array containing the constants of this enum type, in the order they're declared.