# setStaticFriction | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / PhysicsMaterialResource / setStaticFriction 
# setStaticFriction
```kotlin
fun setStaticFriction(staticFriction: Float)
```
Sets the static friction of the physics material. 
#### Parameters
static Friction 
The static friction for the physics material, clamped to the range [0, +∞). The default value is  0.6f . 
#### Throws
Illegal State Exception 
If this resource is closed or invalid.