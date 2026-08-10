# remove | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshInstancesResource / remove 
# remove
```kotlin
fun remove(id: String): Boolean
```
Removes an instance from the resource. 
#### Return
Whether the instance is removed successfully. 
#### Parameters
id 
The ID of the instance to remove. 
#### Throws
Illegal State Exception 
If this resource is closed or invalid.