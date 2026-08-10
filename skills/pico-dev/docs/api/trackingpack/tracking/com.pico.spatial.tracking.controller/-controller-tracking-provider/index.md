# ControllerTrackingProvider | PICO Spatial SDK

tracking / com.pico.spatial.tracking.controller / ControllerTrackingProvider 
# ControllerTrackingProvider
```kotlin
@RequiredFullSpace
```class  ControllerTrackingProvider  :  DataProvider < ControllerTrackingData >  
Provider for controller tracking data and action callbacks; see  DataProvider . 
- 
Tracking data: 6DoF poses for left/right controllers (see  ControllerTrackingData.left / ControllerTrackingData.right ) 
- 
Action callback: button/trigger/grip/thumbstick states (see  ControllerActionListener ) 
Threading/timing: callbacks are invoked on the data source thread at device output rate. Avoid heavy work or blocking inside callbacks; copy data and process on your own thread. 
Members 
## Constructors
Controller Tracking Provider 
```kotlin
constructor()
```
## Types
Controller Action Listener 
```kotlin
fun interface ControllerActionListener
```
Listener interface for controller actions. 
## Functions
add Controller Action Listener 
```kotlin
fun addControllerActionListener(listener: ControllerTrackingProvider.ControllerActionListener)
```
Adds a controller action listener. 
remove Controller Action Listener 
```kotlin
fun removeControllerActionListener(listener: ControllerTrackingProvider.ControllerActionListener)
```
Removes a controller action listener.