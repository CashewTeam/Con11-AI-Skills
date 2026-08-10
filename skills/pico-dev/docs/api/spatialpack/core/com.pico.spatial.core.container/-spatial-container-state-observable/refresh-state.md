# refreshState | PICO Spatial SDK

core / com.pico.spatial.core.container / SpatialContainerStateObservable / refreshState 
# refreshState
```kotlin
fun refreshState(context: Context)
```
Manually refreshes the state of the  SpatialContainer  when state change events are missed. For example, you can call this function when default  WindowContainer 's state has changed before the first  android.app.Activity  listens to it. 
#### Parameters
context 
The context for retrieving the  SpatialContainer .