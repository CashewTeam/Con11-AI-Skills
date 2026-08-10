# kinematicCollisionReportMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PhysicsWorldComponent / kinematicCollisionReportMode 
# kinematicCollisionReportMode
```kotlin
var kinematicCollisionReportMode: KinematicCollisionReportMode
```
Controls whether collisions involving kinematic rigid bodies are reported as  CollisionEvents . 
Default is  KinematicCollisionReportMode.NONE . In this mode, collision events are reported only for collision pairs where at least one rigid body is dynamic. 
This setting applies to the entire physics world managed by this  PhysicsWorldComponent  (i.e., entities that share this component through the entity hierarchy).