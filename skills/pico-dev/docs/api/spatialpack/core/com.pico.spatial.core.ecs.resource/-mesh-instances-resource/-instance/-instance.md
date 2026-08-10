# Instance | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshInstancesResource / Instance / Instance 
# Instance
```kotlin
constructor(id: String, transform: Transform)
```
Creates an instance with the specified unique ID and transform. 
#### Parameters
id 
The ID for the instance. 
transform 
The transform matrix defining the position, rotation, and scale of the instance. 
```kotlin
constructor(id: String, transform: Transform, customFloatData: FloatArray)
```
Creates an instance with the specified unique ID, transform and custom float data.