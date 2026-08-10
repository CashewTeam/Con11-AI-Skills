# onControllerAction | PICO Spatial SDK

tracking / com.pico.spatial.tracking.controller / ControllerTrackingProvider / ControllerActionListener / onControllerAction 
# onControllerAction
```kotlin
abstract fun onControllerAction(action: ControllerActionData)
```
Called for each controller action snapshot. 
#### Parameters
action 
Snapshot for both controllers in the current frame; may be unchanged from the previous frame.