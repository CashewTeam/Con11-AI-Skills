# CONTINUOUS | PICO Spatial SDK

core / com.pico.spatial.core.ecs.simulation / CollisionDetectionMode / CONTINUOUS 
# CONTINUOUS
```kotlin
CONTINUOUS
```
Continuous collision detection with static objects only. This mode has the following characteristics: 
- 
Helps prevent tunneling when interacting with static objects. 
- 
Dynamic objects will still use discrete collision detection with each other. 
- 
Provides a good balance of performance and accuracy.