# PhysicsVelocityComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PhysicsVelocityComponent 
# PhysicsVelocityComponent
```kotlin
@MainThread
```class  PhysicsVelocityComponent  :  Component 
A  Component  that directly sets an entity’s linear and angular velocities. 
This component applies a one-time, instantaneous change in motion (like an impulse) rather than continuously setting a constant velocity or force. Linear and angular velocities are measured in meters per second (m/s) and radians per second (rad/s), respectively, and are applied in world coordinate space. 
To work properly, the entity must also have a  CollisionComponent  and a  RigidBodyComponent . The  rigidBodyMode  of the  RigidBodyComponent  can be set to either  RigidBodyMode.KINEMATIC  or  RigidBodyMode.DYNAMIC . 
Members 
## Constructors
Physics Velocity Component 
```kotlin
constructor()
```
Default constructor. 
```kotlin
constructor(linearVelocity: Vector3, angularVelocity: Vector3)
```
Creates a  PhysicsVelocityComponent  with the specified velocities. 
## Properties
angular Velocity 
```kotlin
var angularVelocity: Vector3
```
The angular velocity of the physics motion around the center of mass, measured in radians per second (rad/s). 
linear Velocity 
```kotlin
var linearVelocity: Vector3
```
The linear velocity of the physics motion in the physics simulation, measured in meters per second (m/s). 
## Functions
clone 
```kotlin
open override fun clone(): Component
```
Creates and returns a copy of this  Component  instance. 
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