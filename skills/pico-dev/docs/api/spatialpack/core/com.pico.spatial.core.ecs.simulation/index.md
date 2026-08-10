# com.pico.spatial.core.ecs.simulation | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation 
# Package-level declarations
Types 
## Types
Collision Cast Hit Mode 
```kotlin
enum CollisionCastHitMode : Enum<CollisionCastHitMode>
```
Specifies the mode for reporting hits in a collision cast query. 
Collision Cast Hit Results 
```kotlin
class CollisionCastHitResults
```
The results of a collision cast. 
Collision Cast Result 
```kotlin
class CollisionCastResult
```
A result of collision cast. 
Collision Contact 
```kotlin
class CollisionContact
```
Provides detailed information about a collision between two objects. 
Collision Detection Mode 
```kotlin
enum CollisionDetectionMode : Enum<CollisionDetectionMode>
```
Specifies the collision detection mode for a physics object. 
Collision Filter 
```kotlin
class CollisionFilter(val group: CollisionGroup = CollisionGroup(COLLISION_GROUP_DEFAULT), val mask: CollisionGroup = CollisionGroup(CollisionGroup.COLLISION_GROUP_ALL))
```
Defines the collision interaction rules between entities using group and mask bitmasks. 
Collision Group 
```kotlin
class CollisionGroup(val value: UInt = COLLISION_GROUP_DEFAULT)
```
Categorizes entities into distinct bitmask-based groups for collision filtering. 
Collision Info Detail Level 
```kotlin
enum CollisionInfoDetailLevel : Enum<CollisionInfoDetailLevel>
```
The enum class that defines what kind of information will be included when a collision object reports this collision event. 
Collision Response Mode 
```kotlin
enum CollisionResponseMode : Enum<CollisionResponseMode>
```
Defines how collision interactions are handled for an entity, including the level of data collected and whether physical collision effects are applied. 
Kinematic Collision Report Mode 
```kotlin
enum KinematicCollisionReportMode : Enum<KinematicCollisionReportMode>
```
Defines whether the collision will be reported when the current kinematic object is colliding with other static or kinematic objects. 
Mass Properties 
```kotlin
class MassProperties
```
Represents the mass properties of a rigid body. 
Rigid Body Mode 
```kotlin
enum RigidBodyMode : Enum<RigidBodyMode>
```
Defines the rigid body modes of an object. 
Simulation Clock 
```kotlin
class SimulationClock
```
A custom clock that drives the physics simulation. By default, the engine clock is used. 
Solver Iterations 
```kotlin
class SolverIterations
```
Defines the iteration counts used by the physics engine when resolving position or velocity constraints.