# Companion | PICO Spatial SDK

core / com.pico.spatial.core.ecs.anchor / AnchorTarget / Companion 
# Companion
```kotlin
object Companion
```
Companion object for  AnchorTarget . 
Members 
## Functions
create Camera Target 
```kotlin
@JvmStatic
```fun  createCameraTarget ( ) :  AnchorTarget 
Creates an  AnchorTarget  instance representing the camera target type. 
create World Anchor Target 
```kotlin
@JvmStatic
```fun  createWorldAnchorTarget ( anchorUUID :  UUID ) :  AnchorTarget 
Creates an  AnchorTarget  instance representing a world anchor identified by a UUID.