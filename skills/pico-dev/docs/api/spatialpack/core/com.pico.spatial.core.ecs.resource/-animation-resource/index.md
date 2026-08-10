# AnimationResource | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AnimationResource 
# AnimationResource
```kotlin
class AnimationResource : Resource
```
The type of animation resource. 
Members 
## Types
Companion 
```kotlin
object Companion
```
The companion object of  AnimationResource . 
## Functions
close 
```kotlin
open override fun close()
```
You need to manually release the resource to free the memory it occupies. 
get Name 
```kotlin
fun getName(): String
```
Gets the name of the animation. 
repeat 
```kotlin
fun repeat(count: Int): AnimationResource
```
Creates a new animation resource with a specified repeat count.