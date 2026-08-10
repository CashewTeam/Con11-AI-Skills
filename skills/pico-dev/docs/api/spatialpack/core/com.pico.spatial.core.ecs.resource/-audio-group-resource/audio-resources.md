# audioResources | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioGroupResource / audioResources 
# audioResources
```kotlin
val audioResources: List<AudioResource>
```
Gets the list of all AudioResources in this audio group. 
This property provides access to all audio resources that have been added to this audio group. The list is fetched from the native/adapter layer and wrapped in  AudioResource  objects. 
#### Return
A list of  AudioResource  objects contained in this group. Returns an empty list if the resource is invalid. 
#### Throws
Illegal Argument Exception 
If this resource has been closed or is invalid.