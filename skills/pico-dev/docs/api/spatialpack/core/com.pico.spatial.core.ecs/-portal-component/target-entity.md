# targetEntity | PICO Spatial SDK

core / com.pico.spatial.core.ecs / PortalComponent / targetEntity 
# targetEntity
```kotlin
var targetEntity: Entity?
```
The target entity representing the world visible through the portal. If  targetEntity  is  null , the portal will not be rendered. To render the portal correctly, set  targetEntity  to a valid  Entity  object.