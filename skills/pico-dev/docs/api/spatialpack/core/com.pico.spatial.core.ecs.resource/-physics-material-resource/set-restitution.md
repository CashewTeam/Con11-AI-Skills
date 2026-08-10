# setRestitution | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicsMaterialResource / setRestitution 
# setRestitution
```kotlin
fun setRestitution(restitution: Float)
```
Sets the restitution of the physics material. 
#### Parameters
restitution 
The restitution for the physics material, clamped to the range 0, 1. The default value is  0f . 
#### Throws
Illegal State Exception 
If this resource is closed or invalid.