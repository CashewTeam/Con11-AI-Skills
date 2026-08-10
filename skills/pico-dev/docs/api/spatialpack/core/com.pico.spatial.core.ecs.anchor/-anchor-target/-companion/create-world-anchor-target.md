# createWorldAnchorTarget | PICO Spatial SDK

core / com.pico.spatial.core.ecs.anchor / AnchorTarget / Companion / createWorldAnchorTarget 
# createWorldAnchorTarget
```kotlin
@JvmStatic
```fun  createWorldAnchorTarget ( anchorUUID :  UUID ) :  AnchorTarget 
Creates an  AnchorTarget  instance representing a world anchor identified by a UUID. 
#### Return
An  AnchorTarget  configured with type  AnchorTargetType.WORLD_ANCHOR  and the given UUID. 
#### Parameters
anchor UUID 
The UUID that identifies the world anchor.