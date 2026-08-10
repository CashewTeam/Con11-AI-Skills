# isOnstage | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform.containers / SpatialContainerStateManager / isOnstage 
# isOnstage
```kotlin
abstract val isOnstage: State<Boolean>
```
Whether the current  SpatialContainer  is onstage. 
A  SpatialContainer  is considered onstage when: 
- 
The camera can view the entire  SpatialContainer  without requiring repositioning. 
- 
The  SpatialContainer  is fully within the camera's perspective, with no overlap or     occlusion caused by other  SpatialContainer  instances.