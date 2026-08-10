# startTransform | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / OrbitAnimation / startTransform 
# startTransform
```kotlin
fun startTransform(startTransform: Transform): OrbitAnimation
```
Set the start transform of the animation. 
#### Return
This  OrbitAnimation  object to allow for method chaining. 
#### Parameters
start Transform 
The start transform of animation. 
```kotlin
var startTransform: Transform
```
The object's initial transform (position / rotation / scale) at animation start. The distance from the orbit center to this position defines the orbit radius. Changing this changes both the starting point and the radius.