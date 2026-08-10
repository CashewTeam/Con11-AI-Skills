# close | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / AudioGroupResource / close 
# close
```kotlin
open override fun close()
```
Closes this audio group resource and releases any native resources. 
This method overrides the parent  AudioAsset.close  method to provide proper resource cleanup. It ensures that the resource is valid before closing and executes the close operation on the schedule thread. 
After calling this method, the resource becomes invalid and any further operations on this resource will throw an  IllegalStateException . 
#### See also
Resource. close