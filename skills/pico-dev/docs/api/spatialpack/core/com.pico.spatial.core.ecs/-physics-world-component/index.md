# PhysicsWorldComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PhysicsWorldComponent 
# PhysicsWorldComponent
```kotlin
@MainThread
```class  PhysicsWorldComponent  :  Component 
A  Component  that creates a new physics world for the entity and allows manipulation of physics simulation parameters including gravity,  KinematicCollisionReportMode ,  SolverIterations , and  SimulationClock . 
Only entities within the same physics world will collide with each other. To put entities in the same physics world, create a parent entity for them and add the  PhysicsWorldComponent  to the parent entity. 
Members 
## Constructors
Physics World Component 
```kotlin
constructor()
```
Default constructor. 
```kotlin
constructor(gravity: Vector3 = Vector3(0.0F, -DEFAULT_GRAVITY_VALUE, 0.0F), kinematicCollisionReportMode: KinematicCollisionReportMode = KinematicCollisionReportMode.NONE, solverIterations: SolverIterations = SolverIterations(positionIterations = 6, velocityIterations = 1), simulationClock: SimulationClock = SimulationClock(fixedTimeStep = 0.02F, maxTimeStep = 0.33F, timeSpeed = 1.0F))
```
Constructs a  PhysicsWorldComponent  with the specified gravity, collision reporting mode, solver iterations, and simulation clock. 
## Properties
gravity 
```kotlin
var gravity: Vector3
```
A tuple of float values that describes the gravity on three axes for the simulation, relative to the simulation entity. The unit is meters per second squared (m/s²). The default value is  Vector3(0.0F, -9.81F, 0.0F) . 
kinematic Collision Report Mode 
```kotlin
var kinematicCollisionReportMode: KinematicCollisionReportMode
```
Controls whether collisions involving kinematic rigid bodies are reported as  CollisionEvents . 
simulation Clock 
```kotlin
var simulationClock: SimulationClock
```
A custom clock driving the physics simulation, defaults to the engine clock. 
solver Iterations 
```kotlin
var solverIterations: SolverIterations
```
The number of iterations that the physics solver uses. 
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