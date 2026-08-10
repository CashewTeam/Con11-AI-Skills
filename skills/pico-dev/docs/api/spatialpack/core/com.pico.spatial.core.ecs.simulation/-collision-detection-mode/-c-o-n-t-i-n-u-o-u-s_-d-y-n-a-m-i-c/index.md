# CONTINUOUS_DYNAMIC | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / CollisionDetectionMode / CONTINUOUS_DYNAMIC 
# CONTINUOUS_DYNAMIC
```kotlin
CONTINUOUS_DYNAMIC
```
Continuous collision detection with both static and dynamic objects. This mode has the following characteristics: 
- 
Prevents tunneling even when colliding with moving objects. 
- 
More computationally expensive than  CONTINUOUS . 
- 
Recommended for fast-moving objects that interact with other dynamic bodies.