# valid | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / valid 
# valid
```kotlin
@get:JvmName(name = "isValid")
```@get: MainThread val  valid :  Boolean 
Indicates whether the current Entity is valid (i.e., not destroyed). 
A valid Entity can be attached to a Scene, have components, and participate in the ECS update loop. Once destroyed, the Entity becomes invalid and should no longer be used. 
#### Return
true  if the entity is attached to a  Scene ;  false  otherwise.