# CollisionFilter | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / CollisionFilter 
# CollisionFilter
```kotlin
class CollisionFilter(val group: CollisionGroup = CollisionGroup(COLLISION_GROUP_DEFAULT), val mask: CollisionGroup = CollisionGroup(CollisionGroup.COLLISION_GROUP_ALL))
```
Defines the collision interaction rules between entities using group and mask bitmasks. 
CollisionFilter  allows fine-grained control over which entities collide. It uses two properties: 
- 
group : Defines what categories this entity belongs to ("Who am I?"). 
- 
mask : Defines what categories this entity can collide with ("What do I hit?"). 
### Collision Rule:
Two entities (Entity A and Entity B) will collide  only if : 
- 
(A.mask AND B.group) != 0  (Entity A is allowed to hit Entity B)  AND 
- 
(B.mask AND A.group) != 0  (Entity B is allowed to hit Entity A) 
### Example:

```
val GROUP_WALL = CollisionGroup(1u shl 0)val GROUP_PLAYER = CollisionGroup(1u shl 1)val GROUP_GHOST = CollisionGroup(1u shl 2)// Player hits walls but not ghostsval playerFilter = CollisionFilter(    group = GROUP_PLAYER,    mask = GROUP_WALL)// Wall hits playersval wallFilter = CollisionFilter(    group = GROUP_WALL,    mask = GROUP_PLAYER)// Ghost doesn't hit anythingval ghostFilter = CollisionFilter(    group = GROUP_GHOST,    mask = CollisionGroup(0u))
```
### Predefined Filters:
- 
COLLISION_FILTER_DEFAULT : Belongs to  CollisionGroup.COLLISION_GROUP_DEFAULT  and collides with everything. 
- 
COLLISION_FILTER_ALL : Belongs to all groups and collides with everything. Useful for sensors or triggers. 
Note: The collision detection system operates with a precision of 0.001 meters (1 millimeter). When the distance between the surfaces of two colliders is less than this threshold, the colliders are considered to be in contact. 
Members 
## Constructors
Collision Filter 
```kotlin
constructor(group: CollisionGroup = CollisionGroup(COLLISION_GROUP_DEFAULT), mask: CollisionGroup = CollisionGroup(CollisionGroup.COLLISION_GROUP_ALL))
```
## Types
Companion 
```kotlin
object Companion
```
The companion object of  CollisionFilter . 
## Properties
group 
```kotlin
val group: CollisionGroup
```
The collision group bitmask this entity belongs to. 
mask 
```kotlin
val mask: CollisionGroup
```
The collision group bitmask that this entity is allowed to collide with. 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```