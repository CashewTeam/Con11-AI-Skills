# orientToPath | PICO Spatial SDK

core / com.pico.spatial.core.ecs.animation / OrbitAnimation / orientToPath 
# orientToPath
```kotlin
fun orientToPath(orientToPath: Boolean): OrbitAnimation
```
Set the orient to path of the animation. 
#### Return
This  OrbitAnimation  object to allow for method chaining. 
#### Parameters
orient To Path 
The orient to path of animation. 
```kotlin
var orientToPath: Boolean
```
If true, the object's orientation continuously aligns to the tangent of its orbital path (i.e., faces direction of motion). If false, orientation is left unchanged (allowing external rotation or "free facing").