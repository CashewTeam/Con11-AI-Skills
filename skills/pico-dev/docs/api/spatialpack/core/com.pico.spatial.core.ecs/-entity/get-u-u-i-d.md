# getUUID | PICO Spatial SDK

core / com.pico.spatial.core.ecs / Entity / getUUID 
# getUUID
```kotlin
@MainThread
```fun  getUUID ( ) :  Long 
Retrieves the globally unique identifier (UUID) of this entity. 
The UUID is a persistent identifier assigned to the entity by the engine. It uniquely identifies the entity across its entire lifecycle. If the entity has been destroyed or is in an invalid state, it may return  0L . 
#### Return
The UUID of the entity, or  0L  if it is unavailable.