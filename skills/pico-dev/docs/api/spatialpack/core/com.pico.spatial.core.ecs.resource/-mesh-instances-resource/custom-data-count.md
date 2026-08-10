# customDataCount | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / MeshInstancesResource / customDataCount 
# customDataCount
```kotlin
val customDataCount: Int
```
The number of custom float values reserved per instance. Range: 0, 16. 
Notes: 
- 
This value is fixed when creating the resource. 
- 
When calling  add  /  update , if the provided  customFloatData  length is greater than this value, an  IllegalArgumentException  will be thrown.