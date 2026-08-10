# addControllerActionListener | PICO Spatial SDK

tracking / com.pico.spatial.tracking.controller / ControllerTrackingProvider / addControllerActionListener 
# addControllerActionListener
```kotlin
fun addControllerActionListener(listener: ControllerTrackingProvider.ControllerActionListener)
```
Adds a controller action listener. 
Registers a global callback with the underlying data source when the first listener is added; subsequent calls only update the local listener list. 
#### Parameters
listener 
Listener to add.