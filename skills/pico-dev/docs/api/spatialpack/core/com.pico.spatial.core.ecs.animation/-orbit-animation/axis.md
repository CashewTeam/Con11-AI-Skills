# axis | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / OrbitAnimation / axis 
# axis
```kotlin
fun axis(axis: Vector3): OrbitAnimation
```
Set the axis of the animation. 
#### Return
This  OrbitAnimation  object to allow for method chaining. 
#### Parameters
axis 
The axis of animation. 
```kotlin
var axis: Vector3
```
Direction vector of the revolution axis (normalized internally). Example: Vector3(0f, 1f, 0f) -> orbit around the world Y axis. Avoid using (0,0,0).