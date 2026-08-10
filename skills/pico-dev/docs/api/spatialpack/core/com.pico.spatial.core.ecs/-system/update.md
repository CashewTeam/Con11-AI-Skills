# update | PICO Spatial SDK

core / com.pico.spatial.core.ecs / System / update 
# update
```kotlin
open fun update(context: SceneUpdateContext)
```
Called periodically by the ECS runtime to update this system. 
You must avoid blocking current callback thread or exchanging other asynchronous threads to execute ECS APIs. 
#### Parameters
context 
The  SceneUpdateContext  associated with this update cycle.