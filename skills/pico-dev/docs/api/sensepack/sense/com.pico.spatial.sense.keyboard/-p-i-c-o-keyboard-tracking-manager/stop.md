# stop | PICO Spatial SDK

sense / com.pico.spatial.sense.keyboard / PICOKeyboardTrackingManager / stop 
# stop
```kotlin
fun stop()
```
Stops the PICO keyboard tracking manager. 
After the manager stops, callers should expect  loadAllAnchors  to return an empty array and should not expect further live updates until  start  is called again.