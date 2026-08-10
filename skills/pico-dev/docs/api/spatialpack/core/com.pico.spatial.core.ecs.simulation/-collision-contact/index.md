# CollisionContact | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / CollisionContact 
# CollisionContact
```kotlin
class CollisionContact
```
Provides detailed information about a collision between two objects. 
Note: The collision detection system operates with a precision of 0.001 meters (1 millimeter). When the distance between the surfaces of two colliders is less than this threshold, the colliders are considered to be in contact. 
Members 
## Constructors
Collision Contact 
```kotlin
constructor(position: Vector3 = Vector3(0.0F, 0.0F, 0.0F), normal: Vector3 = Vector3(0.0F, 0.0F, 0.0F), impulse: Vector3 = Vector3(0.0F, 0.0F, 0.0F), penetrationDistance: Float = 0.0f)
```
## Properties
impulse 
```kotlin
var impulse: Vector3
```
The collision impulse applied at the contact point, measured in newton-seconds (N·s). 
normal 
```kotlin
var normal: Vector3
```
The normal of the contacting surfaces at the contact point. The normal points from the second object toward the first object. The default value is  {0.0f, 0.0f, 0.0f} . 
penetration Distance 
```kotlin
var penetrationDistance: Float
```
The penetration depth between the two colliding objects. 
position 
```kotlin
var position: Vector3
```
The estimated point of contact for a collision. The default value is  {0.0f, 0.0f, 0.0f} .