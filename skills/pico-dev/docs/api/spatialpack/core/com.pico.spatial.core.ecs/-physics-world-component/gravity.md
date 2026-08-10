# gravity | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PhysicsWorldComponent / gravity 
# gravity
```kotlin
var gravity: Vector3
```
A tuple of float values that describes the gravity on three axes for the simulation, relative to the simulation entity. The unit is meters per second squared (m/s²). The default value is  Vector3(0.0F, -9.81F, 0.0F) .