# removeControllerActionListener | PICO Spatial SDK

tracking / com.pico.spatial.tracking.controller / ControllerTrackingProvider / removeControllerActionListener 
# removeControllerActionListener
```kotlin
fun removeControllerActionListener(listener: ControllerTrackingProvider.ControllerActionListener)
```
Removes a controller action listener. 
When the list becomes empty, the global callback is removed from the underlying data source to save resources. 
#### Parameters
listener 
Listener to remove.