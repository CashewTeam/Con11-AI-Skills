# PhysicsWorldComponent | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PhysicsWorldComponent / PhysicsWorldComponent 
# PhysicsWorldComponent
```kotlin
constructor()
```
Default constructor. 
```kotlin
constructor(gravity: Vector3 = Vector3(0.0F, -DEFAULT_GRAVITY_VALUE, 0.0F), kinematicCollisionReportMode: KinematicCollisionReportMode = KinematicCollisionReportMode.NONE, solverIterations: SolverIterations = SolverIterations(positionIterations = 6, velocityIterations = 1), simulationClock: SimulationClock = SimulationClock(fixedTimeStep = 0.02F, maxTimeStep = 0.33F, timeSpeed = 1.0F))
```
Constructs a  PhysicsWorldComponent  with the specified gravity, collision reporting mode, solver iterations, and simulation clock. 
#### Parameters
gravity 
A tuple of float values that describes the gravity on three axes relative to the simulation entity. The default value is  Vector3(0.0F, -9.81F, 0.0F) . 
kinematic Collision Report Mode 
Controls whether collisions involving kinematic rigid bodies are reported as  CollisionEvents . Default is  KinematicCollisionReportMode.NONE . 
solver Iterations 
The number of iterations that the physics solver uses. The default value is  SolverIterations(positionIterations = 6, velocityIterations = 1) . 
simulation Clock 
The  SimulationClock  driving the physics simulation. Defaults to the engine clock:  SimulationClock(fixedTimeStep = 0.02F, maxTimeStep = 0.33F, timeSpeed = 1.0F) .