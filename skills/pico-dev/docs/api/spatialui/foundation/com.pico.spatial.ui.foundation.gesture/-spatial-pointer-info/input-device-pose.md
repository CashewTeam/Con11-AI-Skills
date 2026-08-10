# inputDevicePose | PICO Spatial SDK

ui:foundation / com.pico.spatial.ui.foundation.gesture / SpatialPointerInfo / inputDevicePose 
# inputDevicePose
```kotlin
val inputDevicePose: InputDevicePose
```
The pose of the input device at the time of the event. 
If the event is not from a device with a pose, the pose will be  InputDevicePose.identity .