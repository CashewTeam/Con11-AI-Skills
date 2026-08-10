# rotationCount | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / OrbitAnimation / rotationCount 
# rotationCount
```kotlin
fun rotationCount(rotationCount: Float): OrbitAnimation
```
Set the rotation count of the animation. 
#### Return
This  OrbitAnimation  object to allow for method chaining. 
#### Parameters
rotation Count 
The rotation count of animation, should be greater than 0. 
```kotlin
var rotationCount: Float
```
Number of full revolutions during the entire animation duration. 1f = 360°, 2f = 720°, fractional values allowed (0.5f = 180°). 0f typically means no rotation (unless defined otherwise by the framework).