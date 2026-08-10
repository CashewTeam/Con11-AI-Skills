# CollisionGroup | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / CollisionGroup 
# CollisionGroup
```kotlin
class CollisionGroup(val value: UInt = COLLISION_GROUP_DEFAULT)
```
Categorizes entities into distinct bitmask-based groups for collision filtering. 
A  CollisionGroup  is represented by a 32-bit unsigned integer where each bit can be treated as a separate collision category. This is used in conjunction with  CollisionFilter  to determine which entities should interact physically. 
### Usage Example:

```
// Define unique categories using bit shiftingval CATEGORY_FLOOR   = 1u shl 0 // 0x0001val CATEGORY_PLAYER  = 1u shl 1 // 0x0002val CATEGORY_PROJECTILE = 1u shl 2 // 0x0004// Create a group for a specific categoryval playerGroup = CollisionGroup(CATEGORY_PLAYER)// Entities can belong to multiple categories by combining themval playerAndProjectile = CollisionGroup(CATEGORY_PLAYER or CATEGORY_PROJECTILE)
```
Note: The collision detection system operates with a precision of 0.001 meters (1 millimeter). When the distance between the surfaces of two colliders is less than this threshold, the colliders are considered to be in contact. 
Members 
## Constructors
Collision Group 
```kotlin
constructor(value: UInt = COLLISION_GROUP_DEFAULT)
```
## Types
Companion 
```kotlin
object Companion
```
The companion object of  CollisionGroup . 
## Properties
value 
```kotlin
val value: UInt
```
The bitmask value of the collision group. Defaults to  COLLISION_GROUP_DEFAULT . 
## Functions
equals 
```kotlin
open operator override fun equals(other: Any?): Boolean
```hash Code 
```kotlin
open override fun hashCode(): Int
```to String 
```kotlin
open override fun toString(): String
```