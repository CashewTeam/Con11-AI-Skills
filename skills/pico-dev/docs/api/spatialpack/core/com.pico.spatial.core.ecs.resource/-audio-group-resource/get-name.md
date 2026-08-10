# getName | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioGroupResource / getName 
# getName
```kotlin
fun getName(): String
```
Gets the name of the audio group resource. 
This method returns the name that was assigned to this audio group resource when it was created. The name is used to identify the group in the resource system. 
#### Return
The name of audio group resource. An empty string will be returned if the audio group resource is invalid. 
#### Throws
Illegal State Exception 
If this resource has been closed or is invalid.