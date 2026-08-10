# RigidBodyComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / RigidBodyComponent 
# RigidBodyComponent
```kotlin
@MainThread
```class  RigidBodyComponent  :  Component 
A  Component  responsible for defining the properties of the rigid body, including its  RigidBodyMode ,  MassProperties ,  CollisionDetectionMode , linear and angular damping, gravity influence, and constraints on translation or rotation in specific directions. 
Members 
## Constructors
Rigid Body Component 
```kotlin
constructor()
```
The default constructor. 
```kotlin
constructor(massProperties: MassProperties, rigidBodyMode: RigidBodyMode)
```
Constructs a  RigidBodyComponent  with the specified  MassProperties  and  RigidBodyMode . 
## Properties
angular Damping 
```kotlin
var angularDamping: Float
```
Controls how fast a dynamic rigid body’s rotational motion approaches the zero rest state. Default value is 0.05. 
collision Detection Mode 
```kotlin
var collisionDetectionMode: CollisionDetectionMode
```
Controls the collision detection mode used in physics simulation. Default value is  CollisionDetectionMode.DISCRETE . 
is Affected By Gravity 
```kotlin
var isAffectedByGravity: Boolean
```
Determines whether the simulated object should be affected by gravitational forces. 
is Rotation Locked 
```kotlin
var isRotationLocked: Bool3
```
A tuple of boolean values that indicates whether the rotation of the rigid body is locked around each of the three axes. 
is Translation Locked 
```kotlin
var isTranslationLocked: Bool3
```
A tuple of boolean values representing whether the rigid body's translation is locked along each of the three axes. The default value is  Bool3(false, false, false) , meaning that translation is not locked along any axis. 
linear Damping 
```kotlin
var linearDamping: Float
```
Controls how fast a dynamic rigid body’s translational motion approaches the zero rest state. Default value is 0.02. 
mass Properties 
```kotlin
var massProperties: MassProperties
```
The rigid body’s  MassProperties , including mass, center of mass, inertia, and orientation of inertia. 
rigid Body Mode 
```kotlin
var rigidBodyMode: RigidBodyMode
```
Defines what will influence the motion of the object. 
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