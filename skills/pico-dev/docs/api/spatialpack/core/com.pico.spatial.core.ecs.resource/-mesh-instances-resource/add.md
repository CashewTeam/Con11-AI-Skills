# add | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshInstancesResource / add 
# add
```kotlin
fun add(instance: MeshInstancesResource.Instance): Boolean
```
Adds a new instance to the resource. 
#### Return
Whether the instance is added successfully. 
#### Parameters
instance 
The instance to add. 
#### Throws
Illegal State Exception 
If this resource is closed or invalid. 
Illegal Argument Exception 
If  instance.customFloatData  length is greater than  customDataCount .