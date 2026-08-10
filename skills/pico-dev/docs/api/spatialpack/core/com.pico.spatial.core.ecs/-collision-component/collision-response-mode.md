# collisionResponseMode | PICO Spatial SDK

core / com.pico.spatial.core.ecs / CollisionComponent / collisionResponseMode 
# collisionResponseMode
```kotlin
var collisionResponseMode: CollisionResponseMode
```
The  CollisionResponseMode  of the  CollisionComponent . Default value is  CollisionResponseMode.COLLIDER_FULL . 
Note: This mode controls physical response (collider vs trigger) and the amount of collision data collected, but it does not override the physics world's collision reporting rules. If both bodies are kinematic/static,  CollisionEvents  may still be suppressed unless kinematic collision reporting is enabled via  PhysicsWorldComponent.kinematicCollisionReportMode .