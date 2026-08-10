# Update | PICO Spatial SDK

core / com.pico.spatial.core.ecs.event / CollisionEvents / Update 
# Update
```kotlin
class Update : Event
```
This event is triggered on every frame when two entities are in contact. 
Members 
## Properties
contacts 
```kotlin
val contacts: MutableList<CollisionContact>
```
The list of collision contacts, available only when the collision reporting option is  CollisionInfoDetailLevel.DETAILED . 
entity A 
```kotlin
val entityA: Entity?
```
The first entity involved in the collision. 
entity B 
```kotlin
val entityB: Entity?
```
The second entity involved in the collision. 
impulse 
```kotlin
val impulse: Vector3
```
The total impulse for this collision pair, calculated by summing all impulses at each contact point. Default value is {0.0f, 0.0f, 0.0f}. 
penetration Distance 
```kotlin
val penetrationDistance: Float
```
The estimated overlap distance between the two colliding entities in scene coordinates. Default value is 0.0F. 
position 
```kotlin
val position: Vector3
```
A position representing the estimated point of contact. Default value is {0.0f, 0.0f, 0.0f}. 
## Functions
to String 
```kotlin
open override fun toString(): String
```