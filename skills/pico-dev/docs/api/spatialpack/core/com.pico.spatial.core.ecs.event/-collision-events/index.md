# CollisionEvents | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / CollisionEvents 
# CollisionEvents
```kotlin
object CollisionEvents
```
Provides events triggered when collisions occur between entities. 
Note: The collision detection system operates with a precision of 0.001 meters (1 millimeter). When the distance between the surfaces of two colliders is less than this threshold, the colliders are considered to be in contact. 
Note: By default, collision events are reported only for collision pairs where at least one rigid body is dynamic. 
Contacts involving only kinematic/static bodies may not trigger CollisionEvents unless kinematic collision reporting is explicitly enabled on the physics world via  PhysicsWorldComponent.kinematicCollisionReportMode . 
For more information on subscribing to scene events, refer to  Scene.subscribe  or  SpatialViewContent.subscribe . 
Members 
## Types
Enter 
```kotlin
class Enter : Event
```
This event is triggered when two entities collide. 
Exit 
```kotlin
class Exit : Event
```
This event is triggered when two objects that are in contact separate. 
Update 
```kotlin
class Update : Event
```
This event is triggered on every frame when two entities are in contact. 
## Properties
collision Event Info 
```kotlin
@JvmField
```var  collisionEventInfo :  String 
The string representation of the current collision event information.