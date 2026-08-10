# SpatialHandControllerHaptic | PICO Spatial SDK

ui:platform / com.pico.spatial.ui.platform / SpatialHandControllerHaptic 
# SpatialHandControllerHaptic
```kotlin
interface SpatialHandControllerHaptic
```
hand controller haptic interface, provide feedback for hand controller haptic when user interact with hand controller, such as press, hover, step, etc. 
Members 
## Functions
feedback 
```kotlin
abstract fun feedback(type: HandControllerHapticType, handController: HandController)
```
feedback hand controller haptic