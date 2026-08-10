# state | PICO Spatial SDK

sense / com.pico.spatial.sense.keyboard / PICOKeyboardTrackingManager / state 
# state
```kotlin
val state: TrackingState
```
Gets the current lifecycle state of the keyboard tracking manager. 
Check this property before calling operations such as  loadAllAnchors  when your code needs to distinguish between  not started ,  running , and  stopped  states. 
#### Return
The current  TrackingState  reported by the underlying keyboard tracking manager.