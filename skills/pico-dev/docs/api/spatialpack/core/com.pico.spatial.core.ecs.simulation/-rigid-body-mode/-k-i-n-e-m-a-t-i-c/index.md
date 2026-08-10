# KINEMATIC | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / RigidBodyMode / KINEMATIC 
# KINEMATIC
```kotlin
KINEMATIC
```
Kinematic mode. In this mode, the  RigidBodyComponent  is unaffected by gravity and does not respond to external forces. 
Note:  CollisionEvents  are reported by default only when the collision pair contains at least one dynamic rigid body. Contacts involving only kinematic/static bodies may not trigger  CollisionEvents  unless kinematic collision reporting is explicitly enabled on the physics world via  PhysicsWorldComponent.kinematicCollisionReportMode .