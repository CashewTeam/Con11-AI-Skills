# PhysicsVelocityComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PhysicsVelocityComponent / PhysicsVelocityComponent 
# PhysicsVelocityComponent
```kotlin
constructor()
```
Default constructor. 
```kotlin
constructor(linearVelocity: Vector3, angularVelocity: Vector3)
```
Creates a  PhysicsVelocityComponent  with the specified velocities. 
#### Parameters
linear Velocity 
The linear velocity of the physics motion in the physics simulation. The default value is  Vector3(0F, 0F, 0F) . 
angular Velocity 
The angular velocity of the physics motion around the center of mass. The default value is  Vector3(0F, 0F, 0F) .