# update | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshInstancesResource / update 
# update
```kotlin
fun update(id: String, transform: Transform): Boolean
```
Updates an instance in the resource. 
#### Return
Whether the instance is updated successfully. 
#### Parameters
id 
The ID of the instance to update. 
transform 
The transform of the instance to update. 
#### Throws
Illegal State Exception 
If this resource is closed or invalid. 
```kotlin
fun update(id: String, transform: Transform, customFloatData: FloatArray): Boolean
```
Updates an instance in the resource with both transform and custom float data. 
#### Return
Whether the instance is updated successfully. 
#### Parameters
id 
The ID of the instance to update. 
transform 
The transform of the instance to update. 
custom Float Data 
The custom float data of the instance to update. 
#### Throws
Illegal State Exception 
If this resource is closed or invalid. 
Illegal Argument Exception 
If  customFloatData  length is greater than  customDataCount .