# SpatialContainerStateManager | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / SpatialContainerStateManager 
# SpatialContainerStateManager
```kotlin
interface SpatialContainerStateManager
```
Provides the  SpatialContainer 's states by  State . 
Members 
## Properties
is Focused 
```kotlin
abstract val isFocused: State<Boolean>
```
Whether the current  SpatialContainer  is focused. 
is Onstage 
```kotlin
abstract val isOnstage: State<Boolean>
```
Whether the current  SpatialContainer  is onstage. 
is Sighted 
```kotlin
abstract val isSighted: State<Boolean>
```
Whether the  SpatialContainer  is sighted within the camera's field of view (FOV).