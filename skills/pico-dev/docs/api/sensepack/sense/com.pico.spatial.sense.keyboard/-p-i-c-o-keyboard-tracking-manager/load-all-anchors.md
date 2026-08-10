# loadAllAnchors | PICO Spatial SDK

sense / com.pico.spatial.sense.keyboard / PICOKeyboardTrackingManager / loadAllAnchors 
# loadAllAnchors
```kotlin
suspend fun loadAllAnchors(): Array<PICOKeyboardAnchor>
```
Loads all currently recognized PICO keyboard anchors asynchronously. 
This function returns a snapshot of the anchors that are currently available from the native keyboard tracking system. It is only meaningful when  state  is  TrackingState.RUNNING . If the manager is not running, this function returns an empty array. 
This API does not force discovery of a keyboard. The physical keyboard must already be detected by the system. In practice, keeping the keyboard visible and within the user's field of view helps ensure the anchor can be loaded successfully. 
#### Return
An array of  PICOKeyboardAnchor  objects representing the currently recognized keyboard anchors. Returns an empty array when no keyboard anchor is available or when the manager is not running.