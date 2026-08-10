# PhysicsForceComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PhysicsForceComponent 
# PhysicsForceComponent
```kotlin
@MainThread
```class  PhysicsForceComponent  :  Component 
A  Component  that applies constant force or torque (in local coordinate space) to drive physics-based motion on an entity. Force is measured in newtons (N). Torque is measured in newton-meters (N·m). 
To work properly, the entity must also have a  CollisionComponent  and a  RigidBodyComponent  with its  rigidBodyMode  set to  RigidBodyMode.DYNAMIC . 
Members 
## Constructors
Physics Force Component 
```kotlin
constructor()
```
Default constructor. 
```kotlin
constructor(force: Vector3, torque: Vector3)
```
Creates a physics force component with the specified force and torque. 
## Properties
force 
```kotlin
var force: Vector3
```
The force applied in the local coordinate to control the motion, measured in Newtons (N). The default value is  Vector3(0F, 0F, 0F) . 
torque 
```kotlin
var torque: Vector3
```
The torque applied in the local coordinate to control the motion, measured in Newton-meters (N·m). The default value is  Vector3(0f, 0f, 0f) . 
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