# isSighted | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / SpatialContainerStateManager / isSighted 
# isSighted
```kotlin
abstract val isSighted: State<Boolean>
```
Whether the  SpatialContainer  is sighted within the camera's field of view (FOV). 
A  SpatialContainer  is considered sighted when any part of it (even a single pixel) is within the current FOV of the camera.