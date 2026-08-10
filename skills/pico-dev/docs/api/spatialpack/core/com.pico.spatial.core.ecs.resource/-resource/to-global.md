# toGlobal | PICO Spatial SDK

core / com.pico.spatial.core.ecs.resource / Resource / toGlobal 
# toGlobal
```kotlin
fun toGlobal()
```
Converts the resource to a global resource. 
After turning the  Resource  instance into a global instance, it will no longer be tied to the lifecycle of any other instance. You need to actively call the  close  method to release the resource. This can be used for resource instances that are required globally and can be released at specific moments.