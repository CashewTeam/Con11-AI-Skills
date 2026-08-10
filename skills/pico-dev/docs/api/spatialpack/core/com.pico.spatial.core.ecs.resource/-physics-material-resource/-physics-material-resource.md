# PhysicsMaterialResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicsMaterialResource / PhysicsMaterialResource 
# PhysicsMaterialResource
```kotlin
constructor(staticFriction: Float = 0.6f, dynamicFriction: Float = 0.6f, restitution: Float = 0.0f)
```
Constructs a  PhysicsMaterialResource  by specifying parameters. 
#### Parameters
static Friction 
The static friction for the physics material, clamped to the range [0, +∞). The default value is  0.6f . 
dynamic Friction 
The dynamic friction for the physics material, clamped to the range [0, +∞). The default value is  0.6f . 
restitution 
The restitution for the physics material, clamped to the range 0, 1. The default value is  0f . 
#### Throws
Resource Loading Exception 
If any error occurs during the loading process.