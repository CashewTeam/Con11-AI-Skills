# setDynamicFriction | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicsMaterialResource / setDynamicFriction 
# setDynamicFriction
```kotlin
fun setDynamicFriction(dynamicFriction: Float)
```
Sets the dynamic friction of the physics material. 
#### Parameters
dynamic Friction 
The dynamic friction for the physics material, clamped to the range [0, +∞). The default value is  0.6f . 
#### Throws
Illegal State Exception 
If this resource is closed or invalid.