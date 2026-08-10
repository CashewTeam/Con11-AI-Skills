# add | PICO Spatial SDK

core / com.pico.spatial.core.ecs / AnimationResourceLibraryComponent / add 
# add
```kotlin
fun add(name: String, animationResource: AnimationResource): Boolean
```
Adds a new animation resource to the library with the specified name. 
Returns  false  if the name already exists. 
#### Return
true  if the resource is added;  false  otherwise. 
#### Parameters
name 
The name of the animation resource. 
animation Resource 
The animation resource to add.